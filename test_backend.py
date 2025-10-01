import backend_functions
from datetime import datetime, timedelta

# Signup new user
print(backend_functions.signup("john", "1234"))

# Login
print(backend_functions.login("john", "1234"))

# Add history
backend_functions.add_history("john", "fever,cough", "flu", 0.95)
print("History added.")

# Add reminder
backend_functions.add_reminder("john", datetime.now() + timedelta(hours=1), "Doctor checkup")
print("Reminder added.")

# Check data.json content
with open("data.json", "r") as f:
    data = f.read()
    print("Current data.json content:")
    print(data)