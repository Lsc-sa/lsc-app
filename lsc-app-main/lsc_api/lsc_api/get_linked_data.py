import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def get_countries(**kwargs):
    lang = kwargs.get("lang", "ar")
    frappe.local.lang = lang

    try:
        countries = frappe.get_all(
            "Country", fields=["name", "country_name"], order_by="country_name ASC"
        )

        country_data = [
            {"name": country["name"], "country_name": frappe._(country["country_name"])}
            for country in countries
        ]
        return {
            "status": "success",
            "nationality": country_data,
        }

    except Exception as e:
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}


@frappe.whitelist(allow_guest=True)
def get_branches(**kwargs):
    lang = kwargs.get("lang", "ar")
    frappe.local.lang = lang
    try:
        branches = frappe.get_all(
            "Branch",
            filters={"Disabled": 0},
            fields=["name"],
            order_by="name ASC",
        )

        for branch in branches:
            branch["branch_name"] = _(branch["name"])

        return {
            "status": "success",
            "branches": branches,
        }

    except Exception as e:
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}


@frappe.whitelist(methods=["GET"])
def get_work_cities(**kwargs):
    lang = kwargs.get("lang", "ar")
    frappe.local.lang = lang
    try:
        territories = frappe.get_all(
            "Territory",
            fields=["name", "territory_name"],
            order_by="territory_name ASC",
        )
        territory_names = [
            {
                "name": territory["name"],
                "territory_name": frappe._(territory["territory_name"]),
            }
            for territory in territories
        ]
        return {
            "status": "success",
            "work_city": territory_names,
        }

    except Exception as e:
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}


@frappe.whitelist(methods=["GET"])
def get_legal_types():
    try:
        legal_types = frappe.get_all(
            "Legal Service Types",
            fields=["name", "legla_service_name"],
            order_by="legla_service_name ASC",
        )
        for legal_type in legal_types:
            legal_type["legla_service_name"] = _(legal_type["legla_service_name"])

        return {
            "status": "success",
            "legal_types": legal_types,
        }

    except Exception as e:
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}


@frappe.whitelist(methods=["GET"])
def get_courts():
    try:
        courts = frappe.get_all(
            "Courts",
            fields=["court_name"],
            order_by="court_name ASC",
        )
        court_names = [court_name["court_name"] for court_name in courts]

        return {
            "status": "success",
            "courts": court_names,
        }

    except Exception as e:
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}
