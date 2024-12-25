import frappe
from frappe import _


@frappe.whitelist(methods=["GET"])
def get_terms():
    params = frappe.local.request.args
    term_name = params.get("term_name")
    user = frappe.session.user
    user_language = frappe.db.get_value("User", {"name": user}, "language")

    if not term_name:
        return {
            "status": "fail",
            "message": "You have to enter term name from Terms and Conditions doctype.",
        }

    try:
        if term_name == "privacy_policy" and user_language == "ar":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Privacy Policy in Arabic"}, "terms"
            )
            return {"status": "success", "term_text": term_text}

        elif term_name == "privacy_policy" and user_language == "en":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Privacy Policy in English"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

        #####################################################################################

        if term_name == "inquiries_policy" and user_language == "en":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Inquiries Policy in English"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

        elif term_name == "inquiries_policy" and user_language == "ar":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Inquiries Policy in Arabic"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

        #####################################################################################

        if term_name == "return_policy" and user_language == "en":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Return Policy in English"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

        elif term_name == "return_policy" and user_language == "ar":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Return Policy in Arabic"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

        #####################################################################################

        if term_name == "terms_of_use" and user_language == "en":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Terms of Use in English"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

        elif term_name == "terms_of_use" and user_language == "ar":
            term_text = frappe.db.get_value(
                "Terms and Conditions", {"name": "Terms of Use in Arabic"}, "terms"
            )
            return {"status": "success", "term_text": term_text, "lang": user_language}

    except frappe.DoesNotExistError:
        return {"status": "error", "message": "Terms not found"}
    except Exception as e:
        frappe.log_error(message=str(e), title="Error Fetching Term Text")
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
