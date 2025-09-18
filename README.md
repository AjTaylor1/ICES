# Email Threat Protection

This is an early version Python project that checks incoming emails and predicts whether they’re safe or potentially phishing/scam attempts.  

It works by combining:
- A basic linear regression model for probability scoring.  
- A custom lightweight AI model that looks for patterns common in phishing emails.  

Together, they give a quick confidence score and a final verdict for each email.

## How to Use
1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   python main.py
  email: "Update your account password now"
    → Score: 0.87 (Likely Phishing)

Email: "Team meeting tomorrow at 9am"
→ Score: 0.14 (Safe)
