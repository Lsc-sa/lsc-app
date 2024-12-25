import frappe
from frappe import _

from frappe.utils.password import check_password

from lsc_api.utils.jwt import generate_jwt_token
from lsc_api.utils.error_handler import handle_error



def generate_keys(user):
    user_details = frappe.get_doc("User", user)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()
    return api_secret



@frappe.whitelist(allow_guest=True)
def login(**kwargs):
    try:
        data = kwargs.get("data")

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Make sure that username or email is required and password is required
        if not username and not email:
            return handle_error("Email or username is required.")

        if not password:
            return handle_error("Password is required.")

        # Check if the user exists or if the password is correct
        user = frappe.db.get_value("User", {"email": email}) if email else frappe.db.get_value("User", {"username": username})

        if user:
            user_doc = frappe.get_doc("User", user)
            if not user_doc.enabled:
                return {"status": "fail", "message": "This user is disabled."}

        try:
            login_manager = frappe.auth.LoginManager()
            login_manager.authenticate(user=user, pwd=password)
            login_manager.post_login()
            user = frappe.get_doc("User", user)
        except:
            frappe.local.response['http_status_code'] = 401
            return {"status": "fail", "message": "Invalid email or password."}
        api_generate = generate_keys(frappe.session.user)
        return {
            "status": "success",
            "sid": frappe.session.sid,
            "api_key": user.api_key,
            "api_secret": api_generate,
            "message": "Login successful.",
        }

    except Exception as e:
        # return e
        return {"status": "error", "message": e}

