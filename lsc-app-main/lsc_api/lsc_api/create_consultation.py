import frappe
from frappe.utils.file_manager import save_file
from frappe.utils import now_datetime
import os

import random


def get_available_employee(date, start_time):
    # Fetch all employees with schedules
    employees = frappe.get_all("Employee", fields=["name", "employee_name"])

    for employee in employees:
        # Check if employee has overlapping appointments
        overlap = frappe.db.sql(
            """
            SELECT name FROM `tabEmployee Appointment`
            WHERE employee = %s
            AND appointment_date = %s
            AND appointment_time <= %s
            AND ADDTIME(appointment_time, SEC_TO_TIME(duration*60)) > %s
            AND docstatus != 2
        """,
            (employee["name"], date, start_time, start_time),
        )
        if not overlap:
            return employee["name"]

    # If no available employees found
    return None


@frappe.whitelist(allow_guest=True)
def create_consultation(**kwargs):
    user = frappe.session.user
    poa_expire_date = None
    # Extract fields from the data
    consultation_name = kwargs.get("consultation_name")
    consultation_type = kwargs.get("consultation_type")
    title = kwargs.get("title")
    description = kwargs.get("description")
    start_time = kwargs.get("start_time")
    end_time = kwargs.get("end_time")
    date = kwargs.get("date")

    # Create client transaction
    customer = frappe.get_doc("Customer", {"custom_user": user})

    if frappe.db.exists("Power of Attornies", {"client": customer.name}):
        poa_expire_date = frappe.db.get_value(
            "Power of Attornies", {"client": customer.name}, "expiry_date"
        )

    client_transaction = frappe.new_doc("Client Transaction")
    if poa_expire_date:
        client_transaction.poa_exp_date = poa_expire_date

    client_transaction.client = customer.name
    client_transaction.item = consultation_name
    client_transaction.status = "New"
    client_transaction.save(ignore_permissions=True)

    # Create consultation
    consultation = frappe.new_doc("Consultation")
    consultation.client_transaction = client_transaction.name
    consultation.client = customer.name
    consultation.legal_advisor_title = title
    consultation.legal_advisor_description = description
    consultation.consultation_type = consultation_type
    consultation.status = "جديد"
    consultation.date = date
    consultation.start_time = start_time
    consultation.end_time = end_time
    # Save the consultation
    consultation.save(ignore_permissions=True)
    

    # Handle the uploaded file
    uploaded_file = frappe.request.files.get("file")
    if uploaded_file:
        # Generate a unique filename using timestamp and original extension
        original_filename = uploaded_file.filename
        timestamp = now_datetime().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{original_filename}"

        # Save the file and attach it to the consultation document
        content = uploaded_file.read()
        saved_file = save_file(
            unique_filename,
            content,
            consultation.doctype,
            consultation.name,
            is_private=1,
        )

        # Append the file URL to the consultation's attachments field
        consultation.append("table_sifh", {"attachments": saved_file.file_url})
        # Save the consultation
        consultation.save(ignore_permissions=True)

    return consultation
