import frappe
__version__ = "0.0.1"


def fetch_notofications():
    user = frappe.session.user
    notifications = frappe.get_all(
        "Notification Log",
        filters={
            "for_user": user,
        },
        fields=[
            "name",
            "subject",
            "type",
            "document_type",
            "document_name",
            "creation",
        ],
        order_by="creation desc",
    )
    frappe.publish_realtime(
        'fetch_notofications',
        {'notifications': notifications},
    )
    
@frappe.whitelist(allow_guest=True)
def get_user_lang(user: str | None = None) -> str:
	"""Set frappe.local.lang from user preferences on session beginning or resumption"""
	user = user or frappe.session.user

	# User.language => Session Defaults => frappe.local.lang => 'en'
	return (
		frappe.get_cached_value("User", user, "language")
		or frappe.db.get_default("lang")
		or frappe.local.lang
		or "en"
	)