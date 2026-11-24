# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "gym"
app_title = "Frappe Gym Fitness Manager"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Gym Fitness Manager - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/gym/css/gym.bundle.css"
app_include_js = "/assets/gym/js/gym.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Gym Fitness Manager Entry": {
        "validate": "gym.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "gym.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "gym.tasks.hourly_sync"
    ],
    "daily": [
        "gym.tasks.daily_reconciliation"
    ],
    "weekly": [
        "gym.tasks.weekly_digest"
    ]
}
