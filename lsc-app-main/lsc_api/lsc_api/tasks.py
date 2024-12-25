import frappe
from frappe.utils import date_diff, today


def check_transactions_on_hold():
    client_transactions = frappe.get_all(
        "Client Transaction",
        filters={"on_hold_check": 0},
        fields=["name", "branch", "on_hold_date"],
    )
    on_hold_settings = frappe.get_doc("Notify On Hold")

    for transaction in client_transactions:
        client_transaction = frappe.get_doc("Client Transaction", transaction.name)

        if client_transaction.on_hold_date:
            diff_in_days = date_diff(today(), client_transaction.on_hold_date)

            if diff_in_days >= on_hold_settings.days_on_hold:
                client_transaction.on_hold_check = 1
                employees = frappe.get_all(
                    "Employee",
                    {
                        "designation": on_hold_settings.designation,
                        "branch": client_transaction.branch,
                    },
                    "user_id",
                )

                for employee in employees:
                    notification_doc = frappe.get_doc(
                        {
                            "doctype": "Notification Log",
                            "subject": f"The client transaction {client_transaction.name} has been on hold for {on_hold_settings.days_on_hold} days!",
                            "email_content": f"The client transaction {client_transaction.name} has been on hold for {on_hold_settings.days_on_hold} days!",
                            "for_user": employee.user_id,
                            "type": "Alert",
                            "document_type": "Client Transaction",
                            "document_name": client_transaction.name,
                        }
                    )
                    notification_doc.insert(ignore_permissions=True)

                client_transaction.save()
            else:
                client_transaction.on_hold_check = 0
                client_transaction.save()
