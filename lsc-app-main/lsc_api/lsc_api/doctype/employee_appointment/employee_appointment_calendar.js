
frappe.views.calendar["Employee Appointment"] = {
	field_map: {
		"start": "start",
		"end": "end",
		"id": "name",
		"title": "employee",
		"allDay": "allDay",
		"eventColor": "color"
	},
	order_by: "appointment_date",
	gantt: true,
	get_events_method: "healthcare.healthcare.doctype.patient_appointment.patient_appointment.get_events"
};