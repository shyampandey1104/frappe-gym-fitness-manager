# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "gym"
app_title = "Frappe Gym Fitness Manager"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Gym Fitness Manager for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/gym/css/gym.bundle.css"
app_include_js = "/assets/gym/js/gym.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "gym.engine.on_document_submit",
        "on_cancel": "gym.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "gym.engine.daily_scheduled_sync"
    ]
}
