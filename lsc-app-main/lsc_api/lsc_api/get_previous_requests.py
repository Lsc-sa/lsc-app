import frappe
from frappe import _
import logging


@frappe.whitelist(methods=["GET"])
def get_previous_requests():
    try:
        user = frappe.session.user

        customer = frappe.get_doc("Customer", {"custom_user": user})
        if not customer:
            return {
                "status": "fail",
                "message": "The user has no Customer record created.",
            }

        requests = frappe.get_all(
            "Client Transaction",
            filters={
                "client": customer.name,
                "status": ["in", ["Done", "Cancelled", "Refund"]],
            },
            fields="name, client, status, item, transaction_type, description, creation",
        )

        for request in requests:
            request["status"] = _(request["status"])
            request["item"] = _(request["item"])
            request["transaction_type"] = _(request["transaction_type"])

        if requests:
            for request in requests:
                if frappe.db.exists("Case", {"client_transaction": request["name"]}):
                    case = frappe.get_doc(
                        "Case", {"client_transaction": request["name"]}
                    )
                    comments = frappe.get_all(
                        "Comment",
                        filters={
                            "reference_doctype": "Case",
                            "reference_name": case.name,
                        },
                        fields=["creation", "comment_type", "content", "owner"],
                    )
                    request["title"] = case.case_name
                    request["description"] = case.case_description

                    for comment in comments:
                        comment["content"] = _(comment["content"])
                    request["comments"] = comments

                if frappe.db.exists(
                    "Cases Study", {"client_transaction": request["name"]}
                ):
                    case_study = frappe.get_doc(
                        "Cases Study", {"client_transaction": request["name"]}
                    )
                    comments = frappe.get_all(
                        "Comment",
                        filters={
                            "reference_doctype": "Cases Study",
                            "reference_name": case_study.name,
                        },
                        fields=["creation", "comment_type", "content", "owner"],
                    )
                    request["title"] = case_study.case_study_title
                    request["description"] = case_study.case_description

                    for comment in comments:
                        comment["content"] = _(comment["content"])
                    request["comments"] = comments

                if frappe.db.exists(
                    "Legal Service", {"client_transaction": request["name"]}
                ):
                    legal_service = frappe.get_doc(
                        "Legal Service", {"client_transaction": request["name"]}
                    )
                    comments = frappe.get_all(
                        "Comment",
                        filters={
                            "reference_doctype": "Legal Service",
                            "reference_name": legal_service.name,
                        },
                        fields=["creation", "comment_type", "content", "owner"],
                    )
                    request["title"] = legal_service.services_type
                    request["description"] = legal_service.description

                    for comment in comments:
                        comment["content"] = _(comment["content"])
                    request["comments"] = comments

                if frappe.db.exists(
                    "Consultation", {"client_transaction": request["name"]}
                ):
                    consultation = frappe.get_doc(
                        "Consultation", {"client_transaction": request["name"]}
                    )
                    comments = frappe.get_all(
                        "Comment",
                        filters={
                            "reference_doctype": "Consultation",
                            "reference_name": consultation.name,
                        },
                        fields=["creation", "comment_type", "content", "owner"],
                    )

                    request["title"] = consultation.legal_advisor_title
                    request["description"] = consultation.legal_advisor_description

                    for comment in comments:
                        comment["content"] = _(comment["content"])
                    request["comments"] = comments

            return {
                "status": "success",
                "requests": requests,
            }
        else:
            return {
                "status": "success",
                "message": "The user has no requests.",
                "requests": [],
            }

    except Exception as e:
        return {
            "status": "error",
            "message": f"An error occurred. {str(e)}",
        }
