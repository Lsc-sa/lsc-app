import frappe
import json


@frappe.whitelist(methods=["PATCH"])
def insert_signature(**kwargs):
    user = frappe.session.user
    base_host = frappe.request.host
    try:
        signature = kwargs.get("signature")

        active_contracts = frappe.get_all(
            "Contract",
            filters={
                "party_user": user,
                "status": "Active",
            },
            fields=["*"],
        )

        for contract in active_contracts:
            frappe.set_value("Contract", contract["name"], "status", "Inactive")

        contracts = frappe.get_all(
            "Contract",
            filters={
                "party_user": user,
                "status": "Unsigned",
            },
            fields=["*"],
        )

        if not contracts:
            return {"status": "fail", "message": "No unsigned contracts available."}

        frappe.set_value("Contract", contracts[0].name, "custom_client", signature)
        frappe.set_value("Contract", contracts[0].name, "is_signed", 1)

        account_spage = frappe.get_all("Account Status Page", {"user": user}, "*")
        frappe.db.set_value(
            "Account Status Page", {"user": user}, "contract_status", "Active"
        )
        frappe.db.commit()

        return {
            "status": "success",
            "height": contracts[0].custom_height,
            "print": f"https://{base_host}/printview?doctype=Contract&name={contracts[0].name}&trigger_print=0&format=Contract%20Print&no_letterhead=0&letterhead=LSC%20Head&settings=%7B%7D&_lang=ar",
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error in insert_signature")

        return {
            "status": "fail",
            "message": "An error occurred while updating the contract. \n"
            + frappe.get_traceback(),
            "error": str(e),
        }
