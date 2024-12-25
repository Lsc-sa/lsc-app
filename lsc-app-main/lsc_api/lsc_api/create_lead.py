import frappe
from frappe import _
from lsc_api.utils.error_handler import handle_error
from frappe.utils import validate_email_address, cint
from lsc_api.utils.validate.phone_number import validate_phone_number


@frappe.whitelist(allow_guest=True)
def create_lead(**kwargs):
    data = kwargs.get("data")

    first_name = data.get("first_name")
    email = data.get("email")
    job_title = data.get("job_title")
    mobile_no = data.get("mobile_no")
    nationality = data.get("nationality")
    city = data.get("city")
    custom_accept_terms = data.get("accept_terms")
    custom_send_updates = data.get("send_updates")

    required_fields = ["email"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return handle_error(f"Missing required fields: {', '.join(missing_fields)}")

    if email:
        validate_email_address(email, throw=True)

    if mobile_no:
        if not validate_phone_number(mobile_no):
            return handle_error("Invalid phone number.")

    new_lead = frappe.get_doc(
        {
            "doctype": "Lead",
            "email_id": email,
            "first_name": first_name,
            "mobile_no": mobile_no,
            "job_title": job_title,
            "city": city,
            "country": nationality,
            "custom_accept_terms":custom_accept_terms,
            "custom_send_updates":custom_send_updates
        }
    )
    new_lead.insert(ignore_permissions=True)

    return {
        "status": "success",
        "message": "Lead registered successfully.",
        "user": {
            "first_name": first_name,
            "email": email,
            "job_title": job_title,
            "mobile_no": mobile_no,
            "city": city,
            "nationality": nationality,
            "custom_accept_terms":custom_accept_terms,
            "custom_send_updates":custom_send_updates
        },
    }
