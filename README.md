🩺 Medimind – AI Health Prediction App

Medimind is an AI-powered health assistance application designed to predict possible diseases based on user symptoms. The app provides causes, remedies, diet suggestions, lifestyle guidance, and personalized health insights.
It also includes features like login/signup, prediction history tracking, reminders, and a clean Streamlit interface.

🚀 Features
🔍 AI Disease Prediction

Enter symptoms (comma-separated)

ML model predicts the most probable disease

Shows confidence score

📌 Health Information

Causes of the predicted disease

Remedies for relief

Diet recommendations

Lifestyle improvements

Health risks (static guidance)

🔐 User System

Login & Signup

Stores user details

Saves health history

⏰ Reminder System

Add reminders for medicines, check-ups, etc.

📄 Downloadable Health Report (PDF)

Auto-generated based on prediction

Includes causes, remedies, lifestyle, risks

🧠 Simple Chatbot (Optional)

Basic guidance for health-related questions

🧬 Tech Stack

Python

Streamlit (Frontend + App Framework)

Scikit-learn / ML model

Pandas & NumPy

Pickle (model loading)

Datetime (reminders)

Custom backend functions

Custom disease information dictionary

📁 Project Structure
Medimind/
│── app.py
│── model.pkl
│── backend_functions.py
│── disease_info.py
│── requirements.txt
│── README.md


app.py → Main Streamlit application
model.pkl → Trained ML model
backend_functions.py → Login, history, reminder functions
disease_info.py → Causes, remedies, diet, lifestyle data

▶️ How to Run the App
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run Streamlit app
streamlit run app.py

📘 Usage Instructions

Create an account or log in

Type your symptoms in text box (e.g., fever, cough, headache)

Click Predict Disease

View:

Predicted disease

Confidence percentage

Causes

Remedies

Diet & lifestyle

Risks

Download PDF health report

Add reminders if needed

🛠 Model Information

Input: Selected symptoms

Output: Disease classification

Training: Encoded symptoms with supervised ML algorithm

Customizable disease dataset

Automatically maps prediction → static information

📌 Future Enhancements

Voice-based symptom input

Doctor chatbot with real medical dataset

Real user health monitoring

Mobile app version

Symptom timeline analytics

Integration with wearable devices

🧑‍💻 Developed By

Martin Jr (AI/ML Intern – Nexila Technologies)
Designed to demonstrate real-world application of AI in healthcare prediction.
