import frappe
from frappe import _
from frappe.utils import now_datetime


@frappe.whitelist(methods=["POST"])
def attach_file(**kwargs):
    try:
        user = frappe.session.user

        customer = frappe.get_doc("Customer", {"custom_user": user})
        if not customer:
            return {
                "status": "fail",
                "message": "The user has no Customer record created.",
            }

        client_trans = kwargs.get("client_transaction")

        file = frappe.request.files.get("file")
        if not file:
            return {
                "status": "fail",
                "message": "No file found in the request.",
            }

        if not client_trans:
            return {
                "status": "fail",
                "message": "Client transaction is mandatory to create a comment..",
            }

        client_transaction = frappe.get_doc("Client Transaction", client_trans)

        if client_transaction:
            if frappe.db.exists(
                "Case", {"client_transaction": client_transaction.name}
            ):
                case = frappe.get_doc(
                    "Case", {"client_transaction": client_transaction.name}
                )
                save_file_to_doc("Case", case.name)

            if frappe.db.exists(
                "Cases Study", {"client_transaction": client_transaction.name}
            ):
                case_study = frappe.get_doc(
                    "Cases Study", {"client_transaction": client_transaction.name}
                )
                save_file_to_doc("Cases Study", case_study.name)

            if frappe.db.exists(
                "Legal Service", {"client_transaction": client_transaction.name}
            ):
                legal_service = frappe.get_doc(
                    "Legal Service",
                    {"client_transaction": client_transaction.name},
                )
                save_file_to_doc("Legal Service", legal_service.name)

            if frappe.db.exists(
                "Consultation", {"client_transaction": client_transaction.name}
            ):
                consultation = frappe.get_doc(
                    "Consultation",
                    {"client_transaction": client_transaction.name},
                )
                save_file_to_doc("Consultation", consultation.name)

            return {
                "status": "success",
                "message": "File attached.",
            }
        else:
            return {
                "status": "fail",
                "message": "Couldn't find details about this transactions.",
            }

    except Exception as e:
        return {
            "status": "error",
            "message": f"An error occurred. {str(e)}",
        }


def save_file_to_doc(doctype, attached_to):
    try:
        uploaded_file = frappe.request.files.get("file")
        if uploaded_file:
            original_filename = uploaded_file.filename
            timestamp = now_datetime().strftime("%Y%m%d%H%M%S")
            unique_filename = f"{timestamp}_{original_filename}"

            content = uploaded_file.read()

            saved_file = frappe.get_doc(
                {
                    "doctype": "File",
                    "file_name": unique_filename,
                    "attached_to_doctype": doctype,
                    "attached_to_name": attached_to,
                    "content": content,
                    "is_private": 1,
                }
            )
            saved_file.insert(ignore_permissions=True)
            frappe.db.commit()
            return saved_file.file_url
        else:
            return {
                "status": "fail",
                "response": f"No file found for {uploaded_file}",
            }

    except Exception as e:
        return {
            "status": "fail",
            "response": f"Error saving file for {uploaded_file}: {str(e)}",
        }
