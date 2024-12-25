import frappe
from frappe import _
import requests
from frappe.utils import today, date_diff


@frappe.whitelist(allow_guest=True)
def get_payment_status(charge_id=None):

    try:
        payment_settings = frappe.get_doc("Payment Settings")
        secret_key = None
        if payment_settings.use_live:
            secret_key = payment_settings.live_secret_key
        else:
            secret_key = payment_settings.test_secret_key

        if not charge_id:
            params = frappe.local.request.args
            charge_id = params.get("id")

        # Payment API request
        url = "https://api.moyasar.com/v1/invoices"
        headers = {
            "Content-Type": "application/json",
        }

        response = requests.get(
            f"{url}/{charge_id}",
            headers=headers,
            auth=(secret_key, ""),
        )

        data = response.json()

        return {"status": data.get("status"), "respone": data}

    except:
        return {"status": "fail", "message": "Something was wrong"}


@frappe.whitelist(allow_guest=True)
def refund():
    current_date = today()

    try:
        user = frappe.session.user
        account_spage = frappe.get_doc("Account Status Page", {"user": user})
        payment_settings = frappe.get_doc("Payment Settings")
        subscription = None
        secret_key = None
        if payment_settings.use_live:
            secret_key = payment_settings.live_secret_key
        else:
            secret_key = payment_settings.test_secret_key

        customer = frappe.get_doc("Customer", {"custom_user": user})

        if frappe.db.exists(
            "Subscription", {"party": customer.name, "status": "Active"}
        ):
            subscription = frappe.get_doc(
                "Subscription", {"party": customer.name, "status": "Active"}
            )
            charge_id = subscription.custom_tap_charge_id
            payment_id = subscription.custom_moyasar_payment_id

            result = get_payment_status(charge_id=charge_id)
            invoice_status = result.get("status")

            amount = result.get("respone").get("amount")

        else:
            return {
                "status": "fail",
                "message": "There is no active subscription for this user..",
            }

        remaining_hrs = frappe.get_all(
            "Quota", {"parent": subscription.name}, "hrs"
        )
        total_remaining_hrs = 0
        for row in remaining_hrs:
            total_remaining_hrs += int(row["hrs"])
        
        plan = frappe.get_doc("Subscription Plan", {"name": subscription.plans[0].plan})
        if int(total_remaining_hrs) != int(plan.custom_total_plan_hrs):
            return {
                "status": "fail",
                "remaining_hrs": total_remaining_hrs,
                "total_hrs": plan.custom_total_plan_hrs,
                "message": "consumed_hours",
            }

        days_diff = date_diff(current_date, subscription.current_invoice_start)
        if days_diff >= 15:
            return {
                "status": "fail",
                "current_date": current_date,
                "subscription_date": subscription.current_invoice_start,
                "date_diff": days_diff,
                "message": "days_diff",
            }

        if invoice_status == "paid":
            url = f"https://api.moyasar.com/v1/payments/{payment_id}/refund"
            headers = {
                "Content-Type": "application/json",
            }

            response = requests.post(
                url,
                headers=headers,
                auth=(secret_key, ""),
            )

            data = response.json()

            frappe.db.set_value(
                "Subscription", {"name": subscription.name}, "status", "Cancelled"
            )
            frappe.db.commit()

            prev_contracts = frappe.get_all("Contract", {"party_user": user}, "name")

            for contract in prev_contracts:
                frappe.db.set_value(
                    "Contract", {"name": contract["name"]}, "status", "Inactive"
                )

            frappe.db.set_value(
                "Account Status Page", {"name": account_spage.name}, "contract", None
            )
            frappe.db.set_value(
                "Account Status Page",
                {"name": account_spage.name},
                "contract_status",
                None,
            )
            frappe.db.set_value(
                "Account Status Page",
                {"name": account_spage.name},
                "status",
                "Incomplete",
            )
            frappe.db.commit()

            return {
                "id": charge_id,
                "amount": amount,
                "status": data.get("status"),
                "respone": data,
            }
        else:
            return {
                "status": "fail",
                "message": "The invoice isn't paid..",
                "invoice_status": invoice_status,
            }

    except Exception as e:
        return {"status": "fail", "message": "Something was wrong", "error": f"{e}"}
