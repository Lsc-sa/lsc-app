import frappe
from frappe.utils.file_manager import save_file
from frappe.utils import now_datetime
import os


@frappe.whitelist(methods=["POST"])
def create_case_study(**kwargs):
    user = frappe.session.user
    poa_expire_date = None
    message = ""
    case_name = kwargs.get("name")
    title = kwargs.get("title")
    case_description = kwargs.get("description")

    customer = frappe.get_doc("Customer", {"custom_user": user})
    if frappe.db.exists("Power of Attornies", {"client": customer.name}):
        poa_expire_date = frappe.db.get_value(
            "Power of Attornies", {"client": customer.name}, "expiry_date"
        )
    else:
        message = ""
        
    client_transaction = frappe.new_doc("Client Transaction")
    if poa_expire_date:
        client_transaction.poa_exp_date = poa_expire_date

    client_transaction.client = customer.name
    client_transaction.item = case_name
    client_transaction.status = "New"
    client_transaction.save(ignore_permissions=True)

    case_study = frappe.new_doc("Cases Study")
    case_study.client_transaction = client_transaction.name
    case_study.case_study_title = title
    case_study.case_description = case_description

    case_study.save(ignore_permissions=True)

    uploaded_file = frappe.request.files.get("file")
    if uploaded_file:
        original_filename = uploaded_file.filename
        timestamp = now_datetime().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{original_filename}"

        content = uploaded_file.read()
        saved_file = save_file(
            unique_filename,
            content,
            case_study.doctype,
            case_study.name,
            is_private=1,
        )

        case_study.append(
            "table_aexy", {"attachments": saved_file.file_url, "description": title}
        )
        client_transaction.append(
            "attatchments", {"attachments": saved_file.file_url, "description": title}
        )

        case_study.save(ignore_permissions=True)
        client_transaction.save(ignore_permissions=True)

    return {
        "status": "success",
        "title": case_study.case_study_title,
        "client_transaction": case_study.client_transaction,
        "creation": case_study.creation,
        "description": case_study.case_description,
    }
