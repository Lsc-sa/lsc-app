import frappe
from frappe import _


@frappe.whitelist()
def get_user_notifications():
    user = frappe.session.user

    notifications = frappe.get_all(
        "Notification Log",
        filters={
            "for_user": user,
            # "read": 0
        },
        fields=[
            "name",
            "owner",
            "subject",
            "type",
            "document_type",
            "document_name",
            "creation",
        ],
        order_by="creation desc",
    )

    for notification in notifications:
        notification["subject"] = _(notification["subject"])

    return notifications
