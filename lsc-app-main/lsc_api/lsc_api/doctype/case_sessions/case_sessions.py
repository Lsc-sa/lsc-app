import frappe
from frappe.model.document import Document
from frappe import _
class CaseSessions(Document):
    

    @frappe.whitelist()
    def set_employee(self, employee):
        # Get the Employee Appointment linked to the case_session
        appointment_name = frappe.db.get_value("Employee Appointment", {"case_session": self.name}, "name")

        if not appointment_name:
            frappe.throw(_("No appointment found linked to this case session."), title=_("Error"))

        try:
            # Fetch the appointment document by name
            appointment = frappe.get_doc("Employee Appointment", appointment_name)

            cancel_existing_todo_for_case_session(self.name)
            # Cancel the appointment by updating its status and calling the cancellation logic
            frappe.db.set_value("Employee Appointment", appointment.name, "status", "Cancelled")
            cancel_appointment(appointment.name)

            # Ensure the new employee exists
            new_employee_doc = frappe.get_doc("Employee", employee)

            # Create a new appointment with the same details but assign the new employee
            new_appointment = frappe.copy_doc(appointment)
            new_appointment.employee = employee
            new_appointment.insert(ignore_permissions=True)

            # Cancel the existing ToDo assigned to the current employee

            # Assign a new ToDo to the newly assigned employee user
            emp_user = frappe.db.get_value("Employee", employee, "user_id")
            if emp_user:
                new_todo = frappe.get_doc({
                    "doctype": "ToDo",
                    "allocated_to": emp_user,
                    "reference_type": "Case Sessions",
                    "reference_name": self.name,
                    "description": _("Case Sessions reassigned to {0}").format(new_employee_doc.employee_name),
                    "status": "Open",
                    "assigned_by": frappe.session.user,
                })
                new_todo.insert(ignore_permissions=True)

            # Log the change
            frappe.msgprint(
                _("Case Sessions {0} has been reassigned to {1}").format(
                    new_appointment.name, new_employee_doc.employee_name
                ),
                title=_("Employee Reassigned"),
            )

        except frappe.DoesNotExistError:
            frappe.throw(_("The appointment or employee you are trying to modify does not exist."), title=_("Error"))
        except Exception as e:
            frappe.log_error(f"Error reassigning employee in appointment: {str(e)}", "Set Employee Error")
            frappe.throw(_("There was an issue updating the employee for the appointment. Please try again."), title=_("Error"))

    def after_insert(self):
        try:
            item = frappe.db.get_value("Client Transaction",{
                "name": frappe.db.get_value("Case", {"name": self.case_name}, "client_transaction")
            }, "item")
            create_appointment_on = frappe.db.get_all("Create Appointment On", ["*"])

            # Fetch client details
            client = frappe.get_doc("Customer", self.client)
            if item in [item.name for item in create_appointment_on]:
                employee_appointment_type = None
                
                # Find the appropriate designation and appointment type based on the item
                for cur_item in create_appointment_on:
                    if item == cur_item.name:
                        employee_appointment_type = cur_item.employee_appointment_type
                                            
                # Prepare employee appointment document
                cur_employee = frappe.get_doc({
                    "doctype": "Employee Appointment",
                    "customer": self.client,
                    "customer_name": client.customer_name,
                    "employee": self.lawyer_name,  # dynamically selected employee
                    "appointment_type": employee_appointment_type or self.employee_appointment_type,
                    "duration": frappe.db.get_value(
                        "Employee Appointment Type",
                        employee_appointment_type or self.employee_appointment_type,
                        "default_duration",
                    ),
                    "appointment_for": "Employee",
                    "appointment_date": self.session_date,
                    "appointment_time": self.session_time,
                    "case_session": self.name,
                    "custom_session_type": "Session",
                    "mode_of_payment": "",  # Potentially set dynamically
                    "paid_amount": "",  # Optionally set dynamically
                    "invoiced": 0,
                })

                # Insert employee appointment, bypassing permission checks
                cur_employee.insert(ignore_permissions=True)

                # Assign task to the employee if user_id is found
                emp_user = frappe.db.get_value("Employee", self.lawyer_name, "user_id")
                if emp_user:
                    cs = frappe.get_doc({
                        "doctype": "ToDo",
                        "allocated_to": emp_user,
                        "reference_type": "Case Sessions",
                        "reference_name": self.name,
                        "description": "Case Sessions Employee Assignment.",
                        "status": "Open",
                        "assigned_by": frappe.session.user,
                    })
                    cs.insert(ignore_permissions=True)
                else:
                    frappe.log_error(f"No user linked to employee {self.lawyer_name}", "Case Session Error")

        except frappe.DoesNotExistError as e:
            frappe.log_error(f"Error creating employee appointment: {str(e)} for Case Session {self.name}", "Case Session Error")
        except Exception as e:
            frappe.log_error(f"Unhandled error in after_insert for Case Session {self.name}: {str(e)}", "Case Session Error")

def cancel_existing_todo_for_case_session(case_session):
    try:
        # Fetch and cancel the ToDo assigned to the original employee for this appointment
        todos = frappe.get_all("ToDo", filters={"reference_name": case_session, "reference_type": "Case Sessions", "status": "Open"}, fields=["name"])
        for todo in todos:
            frappe.db.set_value("ToDo", todo.name, "status", "Cancelled")
    except Exception as e:
        frappe.log_error(f"Error cancelling ToDo for Case Sessions {case_session}: {str(e)}", "Cancel ToDo Error")

def cancel_appointment(appointment_id):
    appointment = frappe.get_doc("Employee Appointment", appointment_id)
    msg = _("Appointment Cancelled.")
    if appointment.event:
        event_doc = frappe.get_doc("Event", appointment.event)
        event_doc.status = "Cancelled"
        event_doc.save()

    frappe.msgprint(msg)
