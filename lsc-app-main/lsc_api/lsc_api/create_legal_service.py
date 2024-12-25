import frappe
from frappe.utils.file_manager import save_file
from frappe.utils import now_datetime
import os


@frappe.whitelist(methods=["POST"])
def create_legal_service(**kwargs):
    user = frappe.session.user
    poa_expire_date = None
    name = kwargs.get("name")
    legal_type = kwargs.get("legal_type")
    description = kwargs.get("description")

    customer = frappe.get_doc("Customer", {"custom_user": user})
    if frappe.db.exists("Power of Attornies", {"client": customer.name}):
        poa_expire_date = frappe.db.get_value(
            "Power of Attornies", {"client": customer.name}, "expiry_date"
        )

    client_transaction = frappe.new_doc("Client Transaction")
    if poa_expire_date:
        client_transaction.poa_exp_date = poa_expire_date

    client_transaction.client = customer.name
    client_transaction.item = name
    client_transaction.status = "New"
    client_transaction.save(ignore_permissions=True)

    legal_service = frappe.new_doc("Legal Service")
    legal_service.client_transaction = client_transaction.name
    legal_service.services_type = legal_type
    legal_service.description = description

    legal_service.save(ignore_permissions=True)

    uploaded_file = frappe.request.files.get("file")
    if uploaded_file:
        original_filename = uploaded_file.filename
        timestamp = now_datetime().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{original_filename}"

        content = uploaded_file.read()
        saved_file = save_file(
            unique_filename,
            content,
            legal_service.doctype,
            legal_service.name,
            is_private=1,
        )

        legal_service.append("attachements", {"attachments": saved_file.file_url})

        legal_service.save(ignore_permissions=True)

    return {
        "status": "success",
        "client_transaction": legal_service.client_transaction,
        "creation": legal_service.creation,
        "type": legal_service.services_type,
    }
