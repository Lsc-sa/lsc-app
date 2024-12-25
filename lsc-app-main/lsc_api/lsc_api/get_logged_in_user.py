import frappe

@frappe.whitelist(allow_guest=True)
def get_logged_in_user():
    return frappe.session.user