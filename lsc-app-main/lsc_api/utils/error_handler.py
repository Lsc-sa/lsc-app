import frappe

def handle_error( message='Bad Request', status_code=400):
    frappe.local.response['http_status_code'] = status_code

    status = "fail"
    if str(status_code).startswith('5'):
        status = "error"

    return {"status": status, "message": message}