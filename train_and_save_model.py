# train_and_save_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier

# ------------------------
# Step 1: Define your symptoms and diseases
# ------------------------
# These should match what you want your app to accept
all_symptoms = ["fever", "cough", "headache", "fatigue"]
diseases = ["Flu", "Cold"]

# ------------------------
# Step 2: Create training data
# ------------------------
# Example training data (1 = symptom present, 0 = absent)
X_train = [
    [1, 0, 1, 0],  # fever + headache
    [0, 1, 0, 1],  # cough + fatigue
    [1, 1, 1, 0],  # fever + cough + headache
    [0, 1, 0, 0],  # only cough
]

y_train = [
    "Flu",
    "Cold",
    "Flu",
    "Cold"
]

# ------------------------
# Step 3: Train the Random Forest model
# ------------------------
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ------------------------
# Step 4: Save the trained model as model.pkl
# ------------------------
MODEL_FILE = "model.pkl"
with open(MODEL_FILE, "wb") as f:
    pickle.dump(model, f)

print(f"Model trained and saved as {MODEL_FILE}")