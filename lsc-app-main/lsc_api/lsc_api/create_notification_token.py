import frappe
from frappe import _
import logging


@frappe.whitelist(methods=["POST"], allow_guest=True)
def create_notification_token(**kwarg):
    try:
        # accessor = kwarg.get("accessor")
        frappe.log_error(message=f"Failed to send notification token : {str(kwarg)}",
            title="Failed to send notification to token")
        token = kwarg.get("token")
        user = kwarg.get("user")
        device_type = kwarg.get("device_type")

        if not device_type:
            return {"status": "fail", "message": "You have to enter device.."}

        # if accessor != "mobile@user.com":
        #     return {"status": "fail", "message": "You're not allowed.."}

        if user:
            if frappe.db.exists("Notifications Token", {"user": user, "token": token}):
                return {
                    "status": "success",
                    "message": "Token was created before",
                    "token": token,
                }

        if not token:
            return {"status": "fail", "message": "Token is mandatory!"}

        new_token = frappe.get_doc(
            {"doctype": "Notifications Token", "user": user, "token": token, "device_type": device_type}
        )
        new_token.insert(ignore_permissions=True)

        return {"status": "success", "message": "Token Created.", "token": token}

    except Exception as e:
        frappe.log_error(message=f"Failed to send notification token {token}: {str(e)}",
                    title="Failed to send notification to token")
        return {
            "status": "fail",
            "message": f"An error occurred. {str(e)}",
        }
