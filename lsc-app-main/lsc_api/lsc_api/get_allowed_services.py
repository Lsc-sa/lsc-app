import frappe
from frappe import _
import re


@frappe.whitelist(allow_guest=True)
def get_allowed_services():
    try:
        settings = frappe.get_doc("Plans Settings")
        settings_table = frappe.get_all(
            "Service Setting", {"parent": settings}, ["service_name", "hrs"]
        )

        translated_services = [
            {"service_name": _(service["service_name"]), "hrs": service["hrs"]}
            for service in settings_table
        ]
        return {"status": "success", "allowed_services": translated_services}

    except Exception as e:
        return {
            "status": "fail",
            "message": f"An error occurred. {str(e)}",
        }
