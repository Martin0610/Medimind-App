import streamlit as st
import numpy as np
import pickle
from datetime import datetime, timedelta
from plyer import notification
import backend_functions
from disease_info import disease_data

# ------------------------
# Page Config and Dark Theme
# ------------------------
st.set_page_config(page_title="Medimind", layout="wide", page_icon="🩺")
st.markdown(
    """
    <style>
    body {
        background-color: #0a0a0a;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #1f1f1f;
        color: #00ffff;
    }
    .stTextInput>div>input {
        background-color: #1f1f1f;
        color: #00ff00;
    }
    .stTextArea>div>textarea {
        background-color: #1f1f1f;
        color: #00ff00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# Load ML Model
# ------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Symptoms list (match your trained model)
all_symptoms = ["fever", "cough", "headache", "fatigue"]  

def convert_symptoms_to_features(symptom_input):
    user_symptoms = [s.strip().lower() for s in symptom_input.split(",")]
    feature_vector = [1 if s in user_symptoms else 0 for s in all_symptoms]
    return np.array(feature_vector)

def predict_disease(symptoms):
    feature_vector = convert_symptoms_to_features(symptoms)
    prediction = model.predict([feature_vector])[0]
    confidence = max(model.predict_proba([feature_vector])[0])
    
    info = disease_data.get(prediction, {})
    causes = info.get("causes", "ℹ Info not available")
    remedies = info.get("remedies", "ℹ Info not available")
    diet = info.get("diet", {})
    lifestyle = info.get("lifestyle", "ℹ Info not available")
    
    return prediction, confidence, causes, remedies, diet, lifestyle

# ------------------------
# Sidebar: Login/Signup
# ------------------------
st.sidebar.title("🔐 Medimind Login / Signup")
menu = st.sidebar.radio("Go to", ["Login", "Signup"])

if menu == "Signup":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Signup"):
        success, msg = backend_functions.signup(username, password)
        if success:
            st.sidebar.success(f"{msg} ✅ Please login now.")
            username = ""
            password = ""
        else:
            st.sidebar.error(f"{msg} ❌")

elif menu == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        success, msg = backend_functions.login(username, password)
        if success:
            st.sidebar.success(f"{msg} ✅ Welcome, {username}!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            username = ""
            password = ""
        else:
            st.sidebar.error(f"{msg} ❌")
            st.session_state['logged_in'] = False

# ------------------------
# Main App
# ------------------------
if 'logged_in' in st.session_state and st.session_state['logged_in']:
    st.title("🩺 Medimind AI Doctor")
    st.subheader("Describe your symptoms (comma separated)")

    symptom_input = st.text_area("e.g., fever, cough", height=50)

    if st.button("Predict Disease"):
        if symptom_input.strip() == "":
            st.warning("⚠ Please enter your symptoms!")
        else:
            pred, conf, causes, remedies, diet, lifestyle = predict_disease(symptom_input)
            st.markdown(f"## 🧪 Prediction: *{pred}*")
            st.markdown(f"*Confidence:* {conf*100:.1f}%")

            st.markdown("### ⚠ Causes")
            st.info(causes)

            st.markdown("### 💊 Remedies")
            st.success(remedies)

            st.markdown("### 🍎 Diet Plan")
            for meal, food in diet.items():
                st.write(f"{meal}:** {food}")

            st.markdown("### 🏃 Lifestyle")
            st.write(lifestyle)

            # Save history
            backend_functions.add_history(
                st.session_state['username'],
                symptom_input,
                pred,
                conf
            )

    st.markdown("---")
    st.subheader("⏰ Add Reminder")
    reminder_note = st.text_input("Reminder Note")
    reminder_time = st.time_input("Reminder Time")
    if st.button("Add Reminder"):
        dt = datetime.combine(datetime.today(), reminder_time)
        backend_functions.add_reminder(st.session_state['username'], dt, reminder_note)
        st.success(f"Reminder will be sent at {dt.strftime('%H:%M')} ⏰")

    # Show upcoming reminders
    st.subheader("📅 Upcoming Reminders")
    data = backend_functions.load_data()
    now = datetime.now()
    for r in data["reminders"]:
        if r["user"] == st.session_state['username']:
            rem_time = datetime.fromisoformat(r['reminder_time'])
            if now >= rem_time - timedelta(hours=1) and now < rem_time:
                st.warning(f"Reminder in 1 hour: {r['note']}")
                notification.notify(
                    title="Medimind Reminder",
                    message=f"Upcoming: {r['note']} in 1 hour",
                    timeout=10
                )