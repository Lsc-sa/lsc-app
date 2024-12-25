import frappe
import requests
import random
import re
import json
from TaqnyatSms import client
from frappe.utils import now, add_to_date, get_datetime


@frappe.whitelist(allow_guest=True, methods=["POST"])
def sms_api(**kwargs):
    phone_number = kwargs.get("phone_number")
    sms_type = kwargs.get("sms_type")

    if phone_number is None:
        return {
            "status": "fail",
            "message": "Phone number is required.",
        }

    if not is_valid_phone_number(phone_number):
        return {
            "status": "fail",
            "message": "Invalid phone number format. Please provide a valid number.",
        }

    bearer_token = "45e5c7c48191852bb9933f8931e08536"
    otp = generate_otp(phone_number)
    sender = "MusanadahIT"
    recipients = [phone_number]
    body = None

    if sms_type == "create_account":
        body = f"{otp} Is your verification code for registering in Musanadah Portal."
    elif sms_type == "forget_password":
        body = f"{otp} Is your verification code for resetting your password in Musanadah Portal."

    taqnyt = client(bearer_token)
    message = taqnyt.sendMsg(body, recipients, sender, scheduled=None)

    if isinstance(message, str):
        try:
            response = json.loads(message)
        except json.JSONDecodeError as e:
            return {
                "status": "fail",
                "message": f"Error decoding JSON response: {str(e)}",
            }
    else:
        response = message

    if response.get("statusCode") == 201:
        return {"status": "success", "message": f"OTP sent successfully!"}
    else:
        return {
            "status": "fail",
            "message": f"Failed to send OTP. Error: {response}",
        }


def is_valid_phone_number(phone_number):
    pattern = r"^9665[0-9]{8}$"
    return re.match(pattern, phone_number)


def generate_otp(phone_number):
    frappe.db.sql(
        """
        UPDATE `tabOTP Generator`
        SET status = 'Expired'
        WHERE phone_number = %s AND status = 'Valid'
    """,
        phone_number,
    )

    otp = str(random.randint(100000, 999999))

    otp_doc = frappe.get_doc(
        {
            "doctype": "OTP Generator",
            "phone_number": phone_number,
            "otp": otp,
            "created_at": now(),
            "expired_at": add_to_date(now(), minutes=5),
            "status": "Valid",
        }
    )
    try:
        otp_doc.insert(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "OTP Generation Error")
        return {"status": "fail", "message": str(e)}

    return otp


@frappe.whitelist(allow_guest=True, methods=["POST"])
def validateOTP(**kwargs):
    rec_otp = kwargs.get("otp")
    rec_phone_number = kwargs.get("phone_number")

    if not rec_otp:
        return {
            "status": "fail",
            "message": "OTP is required.",
        }

    if not rec_phone_number:
        return {
            "status": "fail",
            "message": "Phone number is required.",
        }

    otp_doc = frappe.db.get_value(
        "OTP Generator",
        filters={"phone_number": rec_phone_number, "status": "Valid"},
        fieldname=["name", "otp", "expired_at"],
        as_dict=True,
    )

    if otp_doc:
        current_time = get_datetime(now())
        otp_expiry_time = get_datetime(otp_doc["expired_at"])
        if current_time > otp_expiry_time:
            return {"status": "fail", "message": "OTP has expired."}

        if rec_otp == otp_doc["otp"]:
            frappe.db.set_value("OTP Generator", otp_doc["name"], "status", "Valid")

            return {
                "status": "success",
                "message": "OTP is correct.",
            }
        else:
            return {"status": "fail", "message": "OTP is incorrect."}
    else:
        return {
            "status": "fail",
            "message": "No valid OTP found for this phone number.",
        }


def expire_otps():
    expired_otps = frappe.db.get_all(
        "OTP Generator",
        filters={"status": "Valid", "expired_at": ("<", now())},
        fields=["name", "expired_at"],
    )

    for otp in expired_otps:
        current_time = get_datetime(now())
        if isinstance(otp["expired_at"], str):
            otp["expired_at"] = get_datetime(otp["expired_at"])

        if otp["expired_at"] < current_time:
            frappe.db.set_value("OTP Generator", otp["name"], "status", "Expired")

    if expired_otps:
        frappe.db.commit()
