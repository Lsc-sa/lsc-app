import frappe


@frappe.whitelist(methods=["POST"])
def disable_user(**kwarg):
    user = frappe.session.user

    access_key = kwarg.get("access_key")

    if access_key == "Disable":
        frappe.local.login_manager.logout()
        frappe.db.set_value("User", {"name": user}, "enabled", 0)
        frappe.db.set_value("User", {"name": user}, "username", None)
        frappe.db.set_value("User", {"name": user}, "mobile_no", None)
        return {"message": "Account got disabled successfully."}

    elif access_key == "Enable":
        frappe.db.set_value("User", {"name": user}, "enabled", 1)
        return {"message": "Account got enabled back successfully."}

    else:
        return {"message": "Wrong access key. I can't help you.."}
