import frappe
from frappe import _
import logging


@frappe.whitelist(allow_guest=True, methods=["POST"])
def set_client_rating(**kwargs):
    client_transaction_name = kwargs.get("name")
    rating = kwargs.get("rating")
    feedback = kwargs.get("feedback")

    if not client_transaction_name:
        return {
            "status": "fail",
            "message": "It's mandatory to pass the name of client transaction..",
        }

    if not rating and not feedback:
        return {
            "status": "fail",
            "message": "You need to enter rating or feedback, one of them at least..",
        }

    if rating:
        frappe.db.set_value(
            "Client Transaction",
            {"name": client_transaction_name},
            "client_rating",
            rating,
        )

    if feedback:
        frappe.db.set_value(
            "Client Transaction",
            {"name": client_transaction_name},
            "client_feedback",
            feedback,
        )

    frappe.db.commit()

    return {"status": "success", "rating": rating, "feedback": feedback}


@frappe.whitelist(allow_guest=True, methods=["GET"])
def get_client_rating(**kwargs):
    client_transaction_name = kwargs.get("name")

    if not client_transaction_name:
        return {
            "status": "fail",
            "message": "It's mandatory to pass the name of client transaction..",
        }

    rating = frappe.db.get_value(
        "Client Transaction", {"name": client_transaction_name}, "client_rating"
    )

    feedback = frappe.db.get_value(
        "Client Transaction", {"name": client_transaction_name}, "client_feedback"
    )

    frappe.db.commit()

    return {"status": "success", "rating": rating, "feedback": feedback}
