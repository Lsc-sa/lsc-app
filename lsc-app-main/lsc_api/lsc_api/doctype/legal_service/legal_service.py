# Copyright (c) 2024, M and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, nowdate, today


class LegalService(Document):
    def after_insert(self):
        client_transaction = frappe.get_doc(
            "Client Transaction", self.client_transaction
        )
        client = client_transaction.client

        # Fetch active subscription for the client
        subscription = frappe.get_all(
            "Subscription",
            filters={"party": client, "status": "Active"},
            fields=["name"],
        )

        if not subscription:
            frappe.throw(f"No active subscription found for client {client}")

        subscription_name = subscription[0].name
        subscription_doc = frappe.get_doc("Subscription", subscription_name)

        # Fetch subscription plan details
        plan_name = subscription_doc.plans[0].plan
        subscription_plan = frappe.get_doc("Subscription Plan", plan_name)

        # Check if item is in allowed services
        allowed_services = [
            service.service_name
            for service in subscription_plan.custom_allowed_services
        ]
        if client_transaction.item not in allowed_services:
            frappe.throw(
                f"Service {client_transaction.item} is not allowed in the subscription plan"
            )

        # Fetch hours required for the service from Plans Setting
        plans_setting = frappe.get_doc("Plans Settings", "Plans Settings")
        service_settings = {
            setting.service_name: setting.hrs
            for setting in plans_setting.service_settings
        }

        if client_transaction.item not in service_settings:
            frappe.throw(
                f"Service {client_transaction.item} not found in Plans Setting"
            )

        required_hours = float(service_settings[client_transaction.item])

        # Check if enough hours are available in the subscription custom quota
        legal_service_quota = None
        for quota in subscription_doc.custom_quota:
            if quota.service_name == "ساعات الخدمات القانونية":
                legal_service_quota = quota
                break

        if not legal_service_quota:
            frappe.throw(f"No legal service hours quota found in the subscription")

        available_hours = float(legal_service_quota.hrs)

        if available_hours < required_hours:
            frappe.throw(
                f"Not enough hours available. Required: {required_hours}, Available: {available_hours}"
            )

        # Deduct the hours from the quota and format as integer
        updated_hours = int(available_hours - required_hours)
        legal_service_quota.hrs = str(updated_hours)

        # Update consumed hours
        consumed_hours = float(legal_service_quota.consumed_hrs or 0)
        legal_service_quota.consumed_hrs = str(int(consumed_hours + required_hours))

        subscription_doc.save()

        comment_settings = frappe.get_doc("Comment Settings")
        comment_samples = frappe.get_all(
            "Comment Samples",
            {"parent": comment_settings, "parentfield": "comment_samples"},
            "service, comment, enabled, language",
        )

        client_transaction = frappe.get_doc(
            "Client Transaction", {"name": self.client_transaction}
        )

        lang = frappe.local.lang
        language = frappe.get_value("Language", {"name": lang}, "language_name")
        language = _(language)
        customer = frappe.get_doc("Customer", {"name": self.client})
        if client_transaction.poa_exp_date:
            poa_exp_date = getdate(client_transaction.poa_exp_date)
            current_date = getdate(today())

            if poa_exp_date < current_date:
                if lang == "ar":
                    poa_status = "غير سارية"
                else:
                    poa_status = "Inactive"
            else:
                if lang == "ar":
                    poa_status = "سارية"
                else:
                    poa_status = "Active"
        else:
            if lang == "ar":
                poa_status = "غير سارية"
            else:
                poa_status = "Inactive"

        context = {
            "service": _(client_transaction.item),
            "client_name": customer.customer_name,
            "lang": language,
            "poa_status": poa_status,
        }
        for sample in comment_samples:
            if sample.service == client_transaction.item and sample.language == lang:
                rendered_template = frappe.render_template(_(sample.comment), context)
                new_comment = frappe.get_doc(
                    {
                        "doctype": "Comment",
                        "comment_type": "Comment",
                        "reference_doctype": self.doctype,
                        "reference_name": self.name,
                        "content": rendered_template,
                    }
                )
                if sample.enabled:
                    new_comment.insert(ignore_permissions=True)


@frappe.whitelist()
def get_allowed_roles_from_settings():
    frappe.flags.ignore_permissions = True

    settings = frappe.get_doc("Comment Settings", "Comment Settings")
    table = frappe.get_all(
        "Roles Table",
        {"parent": settings, "parentfield": "legal_service_allowed_roles"},
        "*",
    )

    allowed_roles = [entry.role for entry in table]

    return allowed_roles
