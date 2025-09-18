from model import train_and_save_model, predict_new_email
from utils import load_emails

if __name__ == "__main__":
    # Train model
    print("Training model...")
    train_and_save_model()

    # Load new emails for prediction
    test_emails = [
        "Congratulations! You won a $1000 gift card. Click here to claim.",
        "Meeting scheduled tomorrow at 10am. Please review the attached agenda.",
        "Verify your account immediately to avoid suspension. Login now."
    ]

    print("\nPredictions:")
    for email in test_emails:
        label, score = predict_new_email(email)
        print(f"Email: {email}\n -> Prediction: {label} (score: {score:.2f})\n")
