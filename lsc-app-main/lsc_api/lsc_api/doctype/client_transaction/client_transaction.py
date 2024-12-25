# Copyright (c) 2024, M and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import today, date_diff


class ClientTransaction(Document):
    def after_insert(self):
        subscription = frappe.get_all(
            "Subscription", filters={"party": self.client, "status": "Active"}, fields=["name"]
        )
        if not subscription:
            frappe.throw(f"No active subscription found for client {self.client}")
            
        subscription_name = subscription[0].name
        subscription_doc = frappe.get_doc("Subscription", subscription_name)
        
        plans_setting = frappe.get_doc("Plans Settings", "Plans Settings")
        service_settings = {
            setting.service_name: setting.hrs for setting in plans_setting.service_settings
        }
        required_hours = float(service_settings[self.item])
        
        cases_quota = None
        consultation_quota = None
        legal_service_quota = None
        
        for quota in subscription_doc.custom_quota:
            if quota.service_name == "ساعات القضايا":
                cases_quota = quota
            elif quota.service_name == "ساعات الاستشارة":
                consultation_quota = quota
            elif quota.service_name == "ساعات الخدمات القانونية":
                legal_service_quota = quota
        
        if "Case" in self.item:
            available_hours = float(cases_quota.hrs)
            if available_hours < required_hours:
                frappe.throw(
                    f"Not enough hours available. Required: {required_hours}, Available: {available_hours}"
                )
        
        elif "Consultation" in self.item:
            available_hours = float(consultation_quota.hrs)
            if available_hours < required_hours:
                frappe.throw(
                    f"Not enough hours available. Required: {required_hours}, Available: {available_hours}"
                )
        
        elif "assist" in self.item:
            available_hours = float(legal_service_quota.hrs)
            if available_hours < required_hours:
                frappe.throw(
                    f"Not enough hours available. Required: {required_hours}, Available: {available_hours}"
                )
                
        customer = frappe.get_doc("Customer", {"name": self.client})
        lang = frappe.db.get_value("User", {"email": customer.custom_user}, "language")
        if lang == "ar":
            notification = frappe.get_doc(
                {
                    "doctype": "Notification Log",
                    "subject": f"تم إنشاء {_(self.item)} بنجاح!",
                    "type": "Alert",
                    "email_content": f"تم إنشاء {_(self.item)} بنجاح!",
                    "document_type": "Client Transaction",
                    "document_name": self.name,
                    "for_user": self.owner,
                }
            )
            notification.insert(ignore_permissions=True)
            frappe.db.commit()
        else:
            notification = frappe.get_doc(
                {
                    "doctype": "Notification Log",
                    "subject": f"{_(self.item)} has been created successfully!",
                    "type": "Alert",
                    "email_content": f"{_(self.item)} has been created successfully!",
                    "document_type": "Client Transaction",
                    "document_name": self.name,
                    "for_user": self.owner,
                }
            )
            notification.insert(ignore_permissions=True)
            frappe.db.commit()
            
        power_of_attorny = frappe.get_all(
            "Power of Attornies",
            {"client": self.client},
            "expiry_date",
        )

        if power_of_attorny:
            self.poa_exp_date = power_of_attorny[0].expiry_date

    def refund(self, type):
        if self.status == "Refund":
            subscription = frappe.get_all(
                "Subscription",
                filters={"party": self.client, "status": "Active"},
                fields=["name"],
            )
            if not subscription:
                frappe.throw(f"No active subscription found for client {self.client}")

            subscription_name = subscription[0].name
            subscription_doc = frappe.get_doc("Subscription", subscription_name)

            plan_name = subscription_doc.plans[0].plan
            subscription_plan = frappe.get_doc("Subscription Plan", plan_name)

            allowed_services = [
                service.service_name
                for service in subscription_plan.custom_allowed_services
            ]

            if self.item not in allowed_services:
                frappe.throw(
                    f"Service {self.item} is not allowed in the subscription plan"
                )

            plans_setting = frappe.get_doc("Plans Settings", "Plans Settings")
            service_settings = {
                setting.service_name: setting.hrs
                for setting in plans_setting.service_settings
            }

            if self.item not in service_settings:
                frappe.throw(f"Service {self.item} not found in Plans Setting")

            required_hours = float(service_settings[self.item])

            cases_quota = None
            for quota in subscription_doc.custom_quota:
                if quota.service_name == type:
                    cases_quota = quota
                    break

            if not cases_quota:
                frappe.throw(f"No cases hours quota found in the subscription")
            available_hours = float(cases_quota.hrs)

            updated_hours = int(available_hours + required_hours)
            cases_quota.hrs = str(updated_hours)

            consumed_hours = float(cases_quota.consumed_hrs or 0)
            cases_quota.consumed_hrs = str(int(consumed_hours - required_hours))
            cases_quota.save()

    def after_submit(self):
        self.checked = 1

    def validate(self):
        diff_in_days = 0

        on_hold_settings = frappe.get_doc("Notify On Hold")
        if self.status == "On Hold" and not self.on_hold_date:
            self.on_hold_date = today()

        if self.status == "On Hold" and self.on_hold_date:
            diff_in_days = date_diff(today(), self.on_hold_date)

        if self.status != "On Hold":
            self.on_hold_date = None
            self.on_hold_check = 0

        if self.status == "Done":
            customer = frappe.get_doc("Customer", {"name": self.client})
            lang = frappe.db.get_value(
                "User", {"email": customer.custom_user}, "language"
            )
            # frappe.msgprint(lang)
            if lang == "ar":
                notification = frappe.get_doc(
                    {
                        "doctype": "Notification Log",
                        "subject": "نقدّر رأيك! 🌟 يرجى تخصيص لحظة لتقييم تجربتك ومشاركة ملاحظاتك. دعمك يساعدنا على التحسين وخدمتك بشكل أفضل!",
                        "type": "Alert",
                        "email_content": "نقدّر رأيك! 🌟 يرجى تخصيص لحظة لتقييم تجربتك ومشاركة ملاحظاتك. دعمك يساعدنا على التحسين وخدمتك بشكل أفضل!",
                        "document_type": "Client Transaction",
                        "document_name": self.name,
                        "for_user": self.owner,
                    }
                )
                notification.insert(ignore_permissions=True)
                frappe.db.commit()
            else:
                notification = frappe.get_doc(
                    {
                        "doctype": "Notification Log",
                        "subject": "We value your opinion! 🌟 Please take a moment to rate your experience and share your feedback. Your support helps us improve and serve you better!",
                        "type": "Alert",
                        "email_content": "We value your opinion! 🌟 Please take a moment to rate your experience and share your feedback. Your support helps us improve and serve you better!",
                        "document_type": "Client Transaction",
                        "document_name": self.name,
                        "for_user": self.owner,
                    }
                )
                notification.insert(ignore_permissions=True)
                frappe.db.commit()

        if frappe.db.exists("Case", {"client_transaction": self.name}):
            frappe.db.set_value(
                "Case",
                {"client_transaction": self.name},
                "client_transaction_status",
                self.status,
            )

            if self.status == "Refund":
                self.refund(type="ساعات القضايا")

        if frappe.db.exists("Cases Study", {"client_transaction": self.name}):
            frappe.db.set_value(
                "Cases Study",
                {"client_transaction": self.name},
                "client_transaction_status",
                self.status,
            )

            if self.status == "Refund":
                self.refund(type="ساعات القضايا")

        if frappe.db.exists("Legal Service", {"client_transaction": self.name}):
            frappe.db.set_value(
                "Legal Service",
                {"client_transaction": self.name},
                "client_transaction_status",
                self.status,
            )

            if self.status == "Refund":
                self.refund(type="ساعات الخدمات القانونية")

        if frappe.db.exists("Consultation", {"client_transaction": self.name}):
            frappe.db.set_value(
                "Consultation",
                {"client_transaction": self.name},
                "client_transaction_status",
                self.status,
            )

            if self.status == "Refund":
                self.refund(type="ساعات الاستشارة")


@frappe.whitelist()
def create_task(source_name, target_doc=None):
    return get_mapped_doc(
        "Client Transaction",
        source_name,
        {
            "Client Transaction": {
                "doctype": "Task",
                "field_map": {
                    "name": "custom_client_transaction",
                    "employee": "custom_employee",
                },
            }
        },
        target_doc,
    )
