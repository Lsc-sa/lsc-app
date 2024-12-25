import frappe
from frappe import _
import logging
import re


@frappe.whitelist(methods=["POST"])
def create_comment(**kwargs):

    try:
        user = frappe.session.user

        customer = frappe.get_doc("Customer", {"custom_user": user})
        if not customer:
            return {
                "status": "fail",
                "message": "The user has no Customer record created.",
            }

        client_trans = kwargs.get("client_transaction")
        comment_content = kwargs.get("comment_content")

        if not comment_content:
            return {"status": "fail", "message": "You didn't pass any comment"}

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
                new_comment = frappe.get_doc(
                    {
                        "doctype": "Comment",
                        "comment_type": "Comment",
                        "reference_doctype": "Case",
                        "reference_name": case.name,
                        "content": comment_content,
                    }
                )
                new_comment.insert(ignore_permissions=True)
                frappe.db.commit()

            if frappe.db.exists(
                "Cases Study", {"client_transaction": client_transaction.name}
            ):
                case_study = frappe.get_doc(
                    "Cases Study", {"client_transaction": client_transaction.name}
                )
                new_comment = frappe.get_doc(
                    {
                        "doctype": "Comment",
                        "comment_type": "Comment",
                        "reference_doctype": "Cases Study",
                        "reference_name": case_study.name,
                        "content": comment_content,
                    }
                )
                new_comment.insert(ignore_permissions=True)
                frappe.db.commit()

            if frappe.db.exists(
                "Legal Service", {"client_transaction": client_transaction.name}
            ):
                legal_service = frappe.get_doc(
                    "Legal Service",
                    {"client_transaction": client_transaction.name},
                )
                new_comment = frappe.get_doc(
                    {
                        "doctype": "Comment",
                        "comment_type": "Comment",
                        "reference_doctype": "Legal Service",
                        "reference_name": legal_service.name,
                        "content": comment_content,
                    }
                )
                new_comment.insert(ignore_permissions=True)
                frappe.db.commit()

            if frappe.db.exists(
                "Consultation", {"client_transaction": client_transaction.name}
            ):
                consultation = frappe.get_doc(
                    "Consultation",
                    {"client_transaction": client_transaction.name},
                )
                new_comment = frappe.get_doc(
                    {
                        "doctype": "Comment",
                        "comment_type": "Comment",
                        "reference_doctype": "Consultation",
                        "reference_name": consultation.name,
                        "content": comment_content,
                    }
                )
                new_comment.insert(ignore_permissions=True)
                frappe.db.commit()

            return {
                "status": "success",
                "message": "Comment created.",
                "content": comment_content,
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
