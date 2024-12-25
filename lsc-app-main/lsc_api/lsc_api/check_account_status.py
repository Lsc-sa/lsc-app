import frappe
from frappe import _
import logging


@frappe.whitelist(methods=["GET"])
def check_account_status():
    try:
        user = frappe.session.user
        base_host = frappe.request.host
        account_spage = frappe.get_all("Account Status Page", {"user": user}, "*")
        subscription_status = None
        customer = frappe.get_doc("Customer", {"custom_user": user})
        active_subscriptions = frappe.get_all(
            "Subscription", {"party": customer.name, "status": "Active"}, "*"
        )

        if not active_subscriptions:
            subscription_status = "Inactive"
        # unset_fields = []
        # exclude_fields = [
        #     "docstatus",
        #     "idx",
        #     "_user_tags",
        #     "_comments",
        #     "_assign",
        #     "_liked_by",
        #     "birthdate",
        #     "passport_number",
        #     "nationality",
        #     "work_city",
        #     "address",
        #     "id_photo",
        #     "iqama_photo",
        # ]
        user_status = "Incomplete"
        contract_status = "Incomplete"
        poa_status = "Incomplete"

        user_fields = [
            "birth_date",
            "custom_nationality",
            "custom_passport_number",
            "custom_work_city",
            "location",
            "custom_customer_ssn_photo",
            "custom_iqama_image",
        ]

        contract_fields = ["contract", "contract_status"]

        poa_fields = ["power_of_attorny", "poa_expiry_date"]

        unset_user_fields = []
        unset_contract_fields = []
        unset_poa_fields = []

        meta = frappe.get_meta("Account Status Page")

        for record in account_spage:
            for field, value in record.items():
                if not value and field in user_fields:
                    unset_user_fields.append(field)
                elif not value and field in contract_fields:
                    unset_contract_fields.append(field)
                elif not value and field in poa_fields:
                    unset_poa_fields.append(field)

        if len(unset_user_fields) == 0:
            user_status = "Complete"
        if len(unset_contract_fields) == 0:
            contract_status = "Complete"
        if len(unset_poa_fields) == 0:
            poa_status = "Complete"

        if (
            user_status == "Complete"
            and contract_status == "Complete"
            and poa_status == "Complete"
        ):
            frappe.db.set_value(
                "Account Status Page", {"user": user}, "status", "Complete"
            )
            frappe.db.commit()

        account_status = frappe.db.get_value(
            "Account Status Page", {"user": user}, "status"
        )
        contract = frappe.db.get_value(
            "Account Status Page", {"user": user}, "contract"
        )

        unset_user_labels = [
            _(meta.get_field(field).label)
            for field in unset_user_fields
            if meta.get_field(field)
        ]

        return {
            "status": "success",
            "account_status": account_status,
            "subscription_status": subscription_status,
            # "active_subscriptions": active_subscriptions,
            "print": f"https://{base_host}/printview?doctype=Contract&name={contract}&trigger_print=0&format=Contract%20Print&no_letterhead=0&letterhead=LSC%20Head&settings=%7B%7D&_lang=ar",
            "user_details": {
                "unset_user_labels": unset_user_labels,
                "user_status": user_status,
            },
            "contract_details": {
                "contract_status": contract_status,
            },
            "attorney_details": {
                "poa_status": poa_status,
            },
        }

    except Exception as e:
        return {
            "status": "fail",
            "message": f"An error occurred. {str(e)}",
        }
