import jwt
import datetime
import frappe

from lsc_api.utils.error_handler import handle_error


# Secret key for JWT
JWT_SECRET = "devsherenomorecry"

def generate_jwt_token(email):
    return jwt.encode(
        {
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
        },
        JWT_SECRET,
        algorithm="HS256",
    )

def handle_error(message, status_code):
    frappe.local.response["http_status_code"] = status_code
    return {
        "message": message,
        "status_code": status_code
    }

@frappe.whitelist(allow_guest=True)
def verify_jwt_middleware(func):
    def wrapper(*args, **kwargs):
        token = frappe.request.headers.get('Authorization')
        if not token:
            return handle_error("Authorization token is missing", 401)
        
        try:
            # Remove 'Bearer ' from the token if present
            token = token.replace('Bearer ', '')
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            frappe.local.jwt_payload = payload  # Store payload in frappe.local for later use
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return handle_error("Token has expired", 401)
        except jwt.InvalidTokenError:
            return handle_error("Invalid token", 401)
        except Exception as e:
            return handle_error(str(e), 401)
    return wrapper


@frappe.whitelist(allow_guest=True)
@verify_jwt_middleware
def get_token():
    token = frappe.local.jwt_payload
    return {"token_payload": token}
