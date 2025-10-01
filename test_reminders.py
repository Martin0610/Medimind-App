from datetime import datetime, timedelta
from plyer import notification
import backend_functions
import time

# Example: Add a reminder for 1 minute from now
user = "john"
reminder_time = datetime.now() + timedelta(minutes=1)
note = "Take medicine"

backend_functions.add_reminder(user, reminder_time, note)
print("Reminder added!")

# Check reminders every 30 seconds
while True:
    data = backend_functions.load_data()
    now = datetime.now()
    for r in data["reminders"]:
        rem_time = datetime.fromisoformat(r["reminder_time"])
        if now >= rem_time - timedelta(hours=1) and now < rem_time:
            notification.notify(
                title="AI Doctor Reminder",
                message=f"Upcoming: {r['note']} in 1 hour",
                timeout=10
            )
            print(f"Notification sent: {r['note']}")
    time.sleep(30)