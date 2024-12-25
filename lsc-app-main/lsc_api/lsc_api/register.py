import frappe
from frappe.utils import validate_email_address, cint
from frappe.utils.password import update_password


from lsc_api.utils.jwt import generate_jwt_token
from lsc_api.utils.validate.password import evaluate_password_strength
from lsc_api.utils.validate.phone_number import validate_phone_number
from lsc_api.utils.error_handler import handle_error

# from frappe.auth import authenticate
from frappe.core.doctype.user.user import generate_keys


@frappe.whitelist(allow_guest=True, methods=["POST"])
def register(**kwargs):
    try:
        # data = frappe.get_doc(kwargs["data"])
        data = kwargs.get("data")

        username = data.get("username")
        first_name = data.get("first_name")
        email = data.get("email")
        password = data.get("password")
        mobile_no = data.get("mobile_no")
        national_id = data.get("national_id")
        branch = data.get("branch")

        # Ensure that the required fields are present
        required_fields = [
            "username",
            "first_name",
            "email",
            "password",
            "mobile_no",
        ]
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return handle_error(f"Missing required fields: {', '.join(missing_fields)}")

        # Validations
        validate_email_address(email, throw=True)

        # 2. Password validation
        password_strength, suggestions = evaluate_password_strength(password)
        if password_strength == "weak":
            return handle_error("Password is too weak. " + " ".join(suggestions))

        elif password_strength == "average":
            return handle_error(
                "Password strength is average. "
                + " ".join(suggestions)
                + " For better security, consider using a stronger password."
            )

        # 3. Phone Number validation
        if not validate_phone_number(mobile_no):
            return handle_error("Invalid phone number.")

        # 4. National ID validation
        if not national_id.isdigit() or len(national_id) > 14 or len(national_id) < 10:
            return handle_error("Invalid National ID.")

        # Make sure that no user is created with the same email, username, phone, or national_id
        if frappe.db.exists("User", {"email": email}):
            return handle_error("User with this email already exists.")

        if frappe.db.exists("User", {"username": username}):
            return handle_error("User with this username already exists.")

        if frappe.db.exists("User", {"mobile_no": mobile_no}):
            return handle_error("User with this phone already exists.")

        if frappe.db.exists("Customer", {"custom_ssn": national_id}):
            return handle_error("User with this national_id already exists.")

        new_user = frappe.get_doc(
            {
                "doctype": "User",
                "email": email,
                "first_name": first_name,
                "full_name": first_name,
                "username": username,
                "mobile_no": mobile_no,
                "enabled": 1,
                "language": "ar",
                "send_welcome_email": 0,
                # "time_zone": "Asia/Suadi",
            }
        )
        new_user.insert(ignore_permissions=True)
        new_user.add_roles("Customer")

        frappe.db.set_value(
            "Notification Settings", {"name": new_user.email}, "user", new_user.email
        )
        frappe.db.commit()

        # Set the password for the user
        update_password(new_user.email, password)
        new_user.save(ignore_permissions=True)
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=new_user.email, pwd=password)
        login_manager.post_login()
        ########################################################### CREATING CUSTOMER FOR THE USER ###########################################################

        new_customer = frappe.get_doc(
            {
                "doctype": "Customer",
                "custom_branch": branch,
                "customer_name": first_name,
                "customer_type": "Individual",
                "custom_user": new_user.name,
                "custom_id_number": national_id,
            }
        )
        new_customer.insert(ignore_permissions=True)

        new_account_status_page = frappe.get_doc(
            {
                "doctype": "Account Status Page",
                "client": new_customer.name,
            }
        )
        new_account_status_page.insert(ignore_permissions=True)

        return {
            "status": "success",
            "message": "User registered successfully.",
            "user": {
                "first_name": first_name,
                "email": email,
                "mobile_no": mobile_no,
            },
        }

    except Exception as e:
        return handle_error(frappe.get_traceback(), 500)
