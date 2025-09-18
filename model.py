import joblib
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "email_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

# Sample dataset for demonstration - Replace with more or CSV
emails = [
    "Win a free iPhone now, click here!",
    "Update your password immediately to secure your account.",
    "Reminder: project meeting tomorrow at 2pm.",
    "Team lunch scheduled for Friday.",
    "Exclusive offer just for you, buy now!",
    "Verify your account information to continue using our service."
]
labels = [1, 1, 0, 0, 1, 1]  # 1 = scam/phish, 0 = safe


def train_and_save_model():
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(emails)

    model = LogisticRegression()
    model.fit(X, labels)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print("Model and vectorizer saved successfully.")


def predict_new_email(email_text):
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError("Model not trained. Run train_and_save_model first.")

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    X_new = vectorizer.transform([email_text])
    prob = model.predict_proba(X_new)[0][1]
    label = "Phishing/Scam" if prob > 0.5 else "Safe"
    return label, prob
