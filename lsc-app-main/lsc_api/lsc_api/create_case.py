import frappe
from frappe.utils.file_manager import save_file
from frappe.utils import now_datetime
import os
from datetime import datetime


@frappe.whitelist(methods=["POST"])
def create_case(**kwargs):
    user = frappe.session.user
    message = None
    poa_expire_date = None
    case_name = kwargs.get("name")
    title = kwargs.get("title")
    case_description = kwargs.get("case_description")

    customer = frappe.get_doc("Customer", {"custom_user": user})

    client_transaction = frappe.new_doc("Client Transaction")
    if poa_expire_date:
        client_transaction.poa_exp_date = poa_expire_date

    client_transaction.client = customer.name
    client_transaction.item = case_name
    client_transaction.status = "New"
    client_transaction.save(ignore_permissions=True)

    case = frappe.new_doc("Case")
    case.raised_at = datetime.now()
    case.client_transaction = client_transaction.name
    case.case_name = title
    case.case_description = case_description

    case.save(ignore_permissions=True)

    if frappe.db.exists("Power of Attornies", {"client": customer.name}):
        poa_expire_date = frappe.db.get_value(
            "Power of Attornies", {"client": customer.name}, "expiry_date"
        )
    else:
        message = f"The user that created {case.doctype}: {case.name} has no power of attorny. Please check the details."
        check_and_notify_user(case)

    uploaded_file = frappe.request.files.get("file")
    if uploaded_file:
        original_filename = uploaded_file.filename
        timestamp = now_datetime().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{original_filename}"

        content = uploaded_file.read()
        saved_file = save_file(
            unique_filename,
            content,
            case.doctype,
            case.name,
            is_private=1,
        )

        case.append("table_wesy", {"attachments": saved_file.file_url})

        case.save(ignore_permissions=True)

    return {
        "status": "success",
        "title": case.case_name,
        "department": case.department,
        "raised_at": case.raised_at,
        "client_transaction": case.client_transaction,
        "message": message if message else "",
    }


def check_and_notify_user(doc):
    assigned_users = frappe.get_all(
        "ToDo",
        filters={
            "reference_type": doc.doctype,
            "reference_name": doc.name,
            "status": "Open",
        },
        fields=["owner"],
    )

    if assigned_users:
        for user in assigned_users:
            frappe.get_doc(
                {
                    "doctype": "Notification Log",
                    "for_user": user["owner"],
                    "subject": "No power of attorny found..",
                    "email_content": f"The user that created {doc.doctype}: {doc.name} has no power of attorny. Please check the details.",
                    "document_type": doc.doctype,
                    "document_name": doc.name,
                }
            ).insert(ignore_permissions=True)

    else:
        frappe.msgprint("No user is assigned to this Case.")
