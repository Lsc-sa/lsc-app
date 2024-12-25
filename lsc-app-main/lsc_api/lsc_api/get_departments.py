import frappe
from frappe import _
import logging


@frappe.whitelist(methods=["GET"])
def get_departments():
    plan_settings = frappe.get_doc("Plans Settings")
    settings_table = frappe.get_all(
        "Service Setting", {"parent": plan_settings}, ["service_name", "hrs"]
    )
    try:
        user = frappe.session.user
        account_spage = frappe.get_all("Account Status Page", {"user": user}, "*")
        account_status = frappe.db.get_value(
            "Account Status Page", {"user": user}, "status"
        )

        departments = frappe.get_all(
            "Item Group", {"parent_item_group": "الأقسام"}, "name"
        )
        customer = frappe.get_doc("Customer", {"custom_user": user})

        if not customer:
            return {
                "status": "fail",
                "message": "The user has no Customer record created.",
            }

        try:
            subscription = frappe.get_doc(
                "Subscription", {"party": customer.name, "status": "Active"}
            )
            plan = subscription.plans[0].plan
        except:
            return {
                "status": "fail",
                "message": "The user has not subscribed yet or has no plans.",
            }

        service_hrs_map = {
            _(setting["service_name"]): setting["hrs"] for setting in settings_table
        }
        services = frappe.get_all("Allowed Service", {"parent": plan}, "service_name")
        services = [
            {"service_name": _(service["service_name"])} for service in services
        ]
        mapped_services = []

        for service in services:
            service_name = service["service_name"]
            if service_name in service_hrs_map:
                mapped_services.append({service_name: service_hrs_map[service_name]})

        service_hrs_map = {
            service_name: hrs
            for service in mapped_services
            for service_name, hrs in service.items()
        }

        for department in departments:
            department_name_translated = _(department["name"])
            items = frappe.get_all(
                "Item",
                filters={"item_group": department.name},
                fields=["name", "item_code", "custom_item_description"],
            )

            items = [
                {
                    "name": _(item["name"]),
                    "custom_item_description": _(item["custom_item_description"]),
                    "item_code": item["item_code"],
                }
                for item in items
            ]

            department["name"] = department_name_translated
            department["details"] = [
                {
                    "name": item["name"],
                    "hrs": service_hrs_map[item["name"]],
                    "description": item["custom_item_description"],
                    "item_code": item["item_code"],
                }
                for item in items
                if item["name"] in service_hrs_map
            ]
        return {
            "status": "success",
            "departments": departments,
            "asp_status": account_status,
        }

    except Exception as e:
        return {
            "status": "fail",
            "message": f"An error occurred. {str(e)}",
        }
