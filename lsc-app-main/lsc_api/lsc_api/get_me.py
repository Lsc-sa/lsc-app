import frappe
from frappe import _

@frappe.whitelist()
def get_me():
    user = frappe.session.user
    if user == "Guest":
        return {"status": "error", "message": "User not logged in"}

    try:
        user_doc = frappe.get_doc("User", user)
        user_data = {
            "email": user_doc.email,
            "first_name": user_doc.first_name,
            "last_name": user_doc.last_name,
            "full_name": user_doc.full_name,
            "phone": user_doc.phone,
            "roles": [role.role for role in user_doc.roles],
            "language": user_doc.language,
            "time_zone": user_doc.time_zone
        }
        return {"status": "success", "data": user_data}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": "User not found"}
    except Exception as e:
        frappe.log_error(message=str(e), title="Error Fetching User Data")
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
