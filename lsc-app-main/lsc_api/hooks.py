app_name = "lsc_api"
app_title = "Lsc Api"
app_publisher = "A O M"
app_description = "LCS API Integration"
app_email = "tanmiyatwebmaster@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lsc_api/css/lsc_api.css"
# app_include_js = "/assets/lsc_api/js/lsc_api.js"

# include js, css files in header of web template
# web_include_css = "/assets/lsc_api/css/lsc_api.css"
# web_include_js = "/assets/lsc_api/js/lsc_api.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lsc_api/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "lsc_api/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "lsc_api.utils.jinja_methods",
# 	"filters": "lsc_api.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lsc_api.install.before_install"
# after_install = "lsc_api.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lsc_api.uninstall.before_uninstall"
# after_uninstall = "lsc_api.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "lsc_api.utils.before_app_install"
# after_app_install = "lsc_api.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "lsc_api.utils.before_app_uninstall"
# after_app_uninstall = "lsc_api.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lsc_api.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# "send_firebase_notification": "frappe.desk.utils.can_be_accessed_by_guest"
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "all": ["lsc_api.lsc_api.sms_api.expire_otps"],
    "daily": ["lsc_api.lsc_api.tasks.check_transactions_on_hold"],
    # "hourly": [
    # 	"lsc_api.tasks.hourly"
    # ],
    # "weekly": [
    # 	"lsc_api.tasks.weekly"
    # ],
    # "monthly": [
    # 	"lsc_api.tasks.monthly"
    # ],
}

# Testing
# -------

# before_tests = "lsc_api.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lsc_api.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lsc_api.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lsc_api.utils.before_request"]
# after_request = ["lsc_api.utils.after_request"]

# Job Events
# ----------
# before_job = ["lsc_api.utils.before_job"]
# after_job = ["lsc_api.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"lsc_api.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [
    {"from_route": "/dashboard/<path:app_path>", "to_route": "dashboard"},
    {"from_route": "/landing/<path:app_path>", "to_route": "landing"},
]

# fixtures = [
#     "Account",
#     "Item Tax Template",
#     "Contract Template",
#     "Sales Taxes and Charges Template",
#     "Subscription Plan",
#     "Custom Field",
#     "Subscription Settings",
#     "Tax Category",
#     "Dashboard Chart",
#     "Custom DocPerm",
#     "Role",
#     "Server Script",
#     "SMS Settings",
#     "System Settings",
#     "Translation",
#     "Email Account",
#     "Email Domain",
#     "Notification",
#     "Item",
#     "Item Price",
#     "Number Card",
#     "KSA VAT Setting",
#     "Property Setter",
#     "ChatGPT Settings",
#     "Comment Settings",
#     "Employee Appointment Type",
#     "Employee Schedule",
#     "Firebase Settings",
#     "Fixed Comment Links",
#     "Legal Service Types",
#     "Payment Settings",
#     "Plans Settings",
#     "Print Format",
#     "Branch",
#     "Designation",
#     "Holiday List",
#     "Item Group",
#     "Terms and Conditions",
#     "Workspace",
#     "File",
#     "Website Settings",
#     "Navbar Settings",
#     "Log Settings"
# ]


doc_events = {
    "*": {
        "on_update": [
            "lsc_api.lsc_api.doctype.assign_by_role.assign_by_role.apply",
            # "lsc_api.lsc_api.doctype.assign_by_role.assign_by_role.update_due_date",
        ],
        "on_cancel": [
            "lsc_api.lsc_api.doctype.assign_by_role.assign_by_role.apply",
        ],
        "on_update_after_submit": [
            "lsc_api.lsc_api.doctype.assign_by_role.assign_by_role.apply",
            # "lsc_api.lsc_api.doctype.assign_by_role.assign_by_role.update_due_date",
        ],
    },
    "Notification Log": {
        "validate": "lsc_api.lsc_api.fcm_token.send_firebase_notification"
    },
    "Comment": {
        "after_insert": "lsc_api.lsc_api.comment_notification.comment_notification",
        "validate": "lsc_api.lsc_api.fcm_token.send_comment_notification",
    },
    # "DocShare": {
    #     "after_insert": "lsc_api.lsc_api.comment_notification.edit_share_checks",
    # }
}
# override_doctype_class = {
#     "Subscription": "lsc_api.overrides.NewSubscription",
#     "Notification": "lsc_api.overrides.CustomNotification",
# }