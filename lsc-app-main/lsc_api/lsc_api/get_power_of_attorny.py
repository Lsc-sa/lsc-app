import frappe


@frappe.whitelist(methods=["GET"])
def get_power_of_attorny():
    user = frappe.session.user

    if frappe.db.exists("Customer", {"custom_user": user}):
        customer = frappe.get_doc("Customer", {"custom_user": user})
    else:
        return {"status": "fail", "message": "Customer not found"}

    responses = frappe.get_all(
        "Power of Attornies",
        {"client": customer.name},
        {"name", "attonery_number__najiz", "expiry_date", "attorney_content"},
    )

    for response in responses:
        files = frappe.get_all("Attachment", {"parent": response.name}, "attachments")
        response["file"] = files

    if responses:
        return {"status": "success", "response": responses}
    else:
        return {"status": "success", "response": "There are no power of attornies"}
