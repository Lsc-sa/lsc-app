import frappe
from frappe import _
import logging


@frappe.whitelist(methods=["GET"])
def get_user_data():
    email = frappe.session.user
    try:
        user_data = frappe.get_all(
            "User",
            filters={"name": email},
            fields=[
                "full_name",
                "username",
                "email",
                "mobile_no",
                "birth_date",
                "location",
                "user_image",
                "language",
            ],
            limit=1,
        )

        if not user_data:
            return {"status": "error", "message": "User not found"}

        user_data = user_data[0]

        customer_data = frappe.get_all(
            "Customer",
            filters={"custom_user": user_data.email},
            fields=[
                "custom_user",
                "custom_id_number",
                "custom_passport_number",
                "custom_nationality",
                "custom_kafeel_name",
                "custom_kafeel_address",
                "custom_salary",
                "custom_work_city",
                "custom_ksa_entering_date",
                "custom_job_contract",
                "custom_customer_ssn_photo_back",
                "custom_customer_ssn_photo",
                "custom_iqama_image",
                "custom_branch",
            ],
        )

        if customer_data:
            customer_data[0]["custom_nationality"] = _(
                customer_data[0]["custom_nationality"]
            )
            customer_data[0]["custom_branch"] = _(customer_data[0]["custom_branch"])
            customer_data[0]["custom_work_city"] = _(
                customer_data[0]["custom_work_city"]
            )
            user_data.update(customer_data[0])

        return {"user_data": user_data}

    except frappe.DoesNotExistError:
        return {"status": "error", "message": "User not found"}
    except Exception as e:
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}
