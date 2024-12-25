import frappe
from frappe import _
from frappe.utils.password import update_password
from frappe.utils import now_datetime


@frappe.whitelist(methods=["PATCH"])
def update_user_data(**kwargs):
    email = frappe.session.user
    try:
        user_data = frappe.get_all(
            "User",
            filters={"name": email},
            fields=["name", "email"],
            limit=1,
        )

        customer_data = frappe.get_all(
            "Customer",
            filters={"custom_user": email},
            fields=["name"],
            limit=1,
        )

        account_page = frappe.get_doc(
            "Account Status Page", {"client": customer_data[0].name}
        )

        if not user_data:
            return {"status": "error", "message": "User not found"}

        user_email = user_data[0].email
        user_fields = [
            "full_name",
            "mobile_no",
            "birth_date",
            "location",
            "user_image",
            "language",
        ]
        if frappe.request.files.get("user_image"):
            file = frappe.request.files.get("user_image")
            file_url = save_file_to_field("User", user_data[0].name, file)
            frappe.db.set_value("User", user_email, "user_image", file_url)

        for field in user_fields:
            if field in kwargs:
                if field == "null":
                    field = None
                frappe.db.set_value("User", user_email, field, kwargs[field])

                if field in ["location", "birth_date"]:
                    frappe.db.set_value(
                        "Account Status Page", account_page.name, field, kwargs[field]
                    )

        if "new_password" in kwargs:
            update_password(user_email, kwargs["new_password"])

        frappe.db.commit()

        if customer_data:
            customer_name = customer_data[0].name

            attach_fields = [
                "custom_job_contract",
                "custom_customer_ssn_photo",
                "custom_customer_ssn_photo_back",
                "custom_iqama_image",
            ]

            for field in attach_fields:
                if frappe.request.files.get(field):
                    file = frappe.request.files.get(field)
                    file_url = save_file_to_field("Customer", customer_name, file)
                    frappe.db.set_value("Customer", customer_name, field, file_url)

                    if field in ["custom_customer_ssn_photo", "custom_iqama_image"]:
                        frappe.db.set_value(
                            "Account Status Page",
                            account_page.name,
                            field,
                            file_url,
                        )

            customer_fields = [
                "custom_id_number",
                "custom_ksa_entering_date",
                "custom_passport_number",
                "custom_nationality",
                "custom_kafeel_name",
                "custom_salary",
                "custom_kafeel_address",
                "custom_work_city",
            ]

            for field in customer_fields:
                if field in kwargs:
                    if field == "null":
                        field = None

                    frappe.db.set_value("Customer", customer_name, field, kwargs[field])
                    if field in [
                        "custom_passport_number",
                        "custom_nationality",
                        "custom_work_city",
                    ]:
                        frappe.db.set_value(
                            "Account Status Page",
                            account_page.name,
                            field,
                            kwargs[field],
                        )

        frappe.db.commit()

        return {
            "status": "success",
            "message": "User and customer data updated successfully",
        }

    except frappe.DoesNotExistError:
        return {"status": "error", "message": "User or Customer not found"}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error in update_user_data API")
        return {"status": "error", "message": f"Something went wrong: {str(e)}"}


def save_file_to_field(doctype, attached_to, uploaded_file):
    try:
        if uploaded_file:
            original_filename = uploaded_file.filename
            timestamp = now_datetime().strftime("%Y%m%d%H%M%S")
            unique_filename = f"{timestamp}_{original_filename}"

            content = uploaded_file.read()

            saved_file = frappe.get_doc(
                {
                    "doctype": "File",
                    "file_name": unique_filename,
                    "attached_to_doctype": doctype,
                    "attached_to_name": attached_to,
                    "content": content,
                    "is_private": 1,
                }
            )
            saved_file.save(ignore_permissions=True)

            return saved_file.file_url
        else:
            return {
                "status": "fail",
                "response": f"No file found for field",
            }

    except Exception as e:
        return {
            "status": "fail",
            "response": f"Error saving file for field: {str(e)}",
        }
