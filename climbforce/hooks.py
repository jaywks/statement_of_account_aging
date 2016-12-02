# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "climbforce"
app_title = "Climbforce"
app_publisher = "Climbforce"
app_description = "for climbforce"
app_icon = "octicon octicon-file-directory"
app_color = "orange"
app_email = "climbforce@frappeapp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/climbforce/css/climbforce.css"
# app_include_js = "/assets/climbforce/js/climbforce.js"

# include js, css files in header of web template
# web_include_css = "/assets/climbforce/css/climbforce.css"
# web_include_js = "/assets/climbforce/js/climbforce.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "climbforce.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "climbforce.install.before_install"
# after_install = "climbforce.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "climbforce.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"climbforce.tasks.all"
# 	],
# 	"daily": [
# 		"climbforce.tasks.daily"
# 	],
# 	"hourly": [
# 		"climbforce.tasks.hourly"
# 	],
# 	"weekly": [
# 		"climbforce.tasks.weekly"
# 	]
# 	"monthly": [
# 		"climbforce.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "climbforce.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "climbforce.event.get_events"
# }

