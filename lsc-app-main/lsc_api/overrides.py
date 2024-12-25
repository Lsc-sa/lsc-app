from datetime import date

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.data import (
    add_days,
    add_months,
    add_to_date,
    cint,
    date_diff,
    flt,
    get_last_day,
    get_link_to_form,
    getdate,
    nowdate,
)
from frappe.email.doctype.notification.notification import Notification
from erpnext.accounts.doctype.subscription.subscription import Subscription

class NewSubscription(Subscription):
    @property
    def get_user_language(self):
        """Returns the language set for the current user."""
        user = self.owner
        if user:
            # Get the user's language from the user document
            user_language = frappe.db.get_value("User", user, "language")
            return user_language or frappe.local.lang  # Fallback to default language
        else:
            # Return default language if no user is logged in
            return frappe.local.lang


class CustomNotification(Notification):
    def get_context(self, doc):
        """
        Extend the context by adding `owner_language` to be used in notifications.
        """
        context = super().get_context(doc)
        # Add owner_language to the context
        context["owner_language"] = self.get_owner_language(doc)
        return context

    def get_owner_language(self, doc):
        """
        Fetch the owner's preferred language from the User doctype.
        Defaults to 'en' if not found.
        """
        if hasattr(doc, "owner") and doc.owner:
            return frappe.db.get_value("User", doc.owner, "language") or "en"
        return "en"

    def evaluate_alert(self, alert, doc, context):
        """
        Evaluate the notification condition with an extended context.
        """
        # Ensure context contains owner_language
        if "owner_language" not in context:
            context["owner_language"] = self.get_owner_language(doc)

        # Log the context for debugging purposes
        frappe.log_error(title="Notification Context Debug", message=str(context))

        try:
            # Safely evaluate the alert condition
            return frappe.safe_eval(alert.condition, None, context)
        except Exception as e:
            # Log the error for troubleshooting
            frappe.log_error(
                message=f"Condition: {alert.condition}, Error: {str(e)}",
                title="Safe Eval Error"
            )
            return False




