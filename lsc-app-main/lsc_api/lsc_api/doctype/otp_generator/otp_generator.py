# Copyright (c) 2024, M and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.query_builder import Interval
from frappe.query_builder.functions import Now

class OTPGenerator(Document):
    @staticmethod
    def clear_old_logs(days=180):
        table = frappe.qb.DocType("Custom Logging Doctype")
        frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
