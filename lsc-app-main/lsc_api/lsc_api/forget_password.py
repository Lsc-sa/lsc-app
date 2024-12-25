import frappe
from frappe.utils.password import update_password


@frappe.whitelist(allow_guest=True)
def verify_mobile(**kwargs):
    mobile_no = kwargs.get("mobile_no")
    if not mobile_no:
        return {"status": "fail", "message": "Mobile number is required."}

    user = frappe.get_value("User", {"mobile_no": mobile_no}, "email")

    if user:
        return {
            "status": "success",
            "message": "There is an user for this mobile number.",
        }
    else:
        return {"status": "fail", "message": "No user found with this mobile number."}


# @frappe.whitelist(allow_guest=True)
# def reset_password(**kwargs):
#     new_password = kwargs.get("new_password")
#     mobile_no = kwargs.get("mobile_no")

#     if not mobile_no or not new_password:
#         return {"status": "fail", "message": f"Mobile_no {mobile_no} and new password {new_password} are required."}

#     user_email = frappe.db.get_value(
#         "User", {"mobile_no": mobile_no}, "email", ignore_permissions=True
#     )

#     if user_email:
#         user = frappe.get_doc("User", {"email": user_email})
#         try:
#             update_password(user=user.name, pwd=new_password)
#             frappe.db.commit()
#             return {"status": "success", "message": "Password updated successfully."}
#         except Exception as e:
#             return {"status": "fail", "message": f"Error updating password: {str(e)}"}
#     else:
#         return {"status": "fail", "message": "No user found with this email."}


@frappe.whitelist(allow_guest=True)
def reset_password(**kwargs):
    new_password = kwargs.get("new_password")
    mobile_no = kwargs.get("mobile_no")

    if not mobile_no or not new_password:
        return {
            "status": "fail",
            "message": f"Mobile_no {mobile_no} and new password {new_password} are required.",
        }

    try:
        user_email = frappe.get_all(
            "User",
            filters={"mobile_no": mobile_no},
            pluck="email",
            ignore_permissions=True,
        )

        if user_email:
            user = frappe.get_doc("User", {"email": user_email[0]})
            update_password(user=user.name, pwd=new_password)
            frappe.db.commit()
            return {"status": "success", "message": "Password updated successfully."}

        else:
            return {"status": "fail", "message": "No user found with this email."}

    except Exception as e:
        return {"status": "fail", "message": f"Error updating password: {str(e)}"}
