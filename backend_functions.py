import json
from datetime import datetime

import os
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "data.json")

# Load JSON data
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {"users": [], "history": [], "reminders": []}
    return data

# Save JSON data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Signup
def signup(username, password):
    data = load_data()
    # Check if username exists safely
    existing_usernames = [u.get("username") for u in data.get("users", [])]
    if username in existing_usernames:
        return False, "Username already exists"
    data["users"].append({"username": username, "password": password})
    save_data(data)
    return True, "Signup successful"

# Login
def login(username, password):
    data = load_data()
    for u in data.get("users", []):   # use get() to avoid KeyError
        if u.get("username") == username and u.get("password") == password:
            return True, "Login successful"
    return False, "Invalid username or password"

# Add history
def add_history(user, symptoms, prediction, confidence):
    data = load_data()
    data["history"].append({
        "user": user,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "symptoms": symptoms,
        "prediction": prediction,
        "confidence": round(confidence*100,1)
    })
    save_data(data)

# Add reminder
def add_reminder(user, reminder_time, note):
    data = load_data()
    data["reminders"].append({
        "user": user,
        "reminder_time": reminder_time.isoformat(),
        "note": note
    })
    save_data(data)