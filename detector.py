
def check_email(email_text):
    suspicious_words = [
        "urgent",
        "verify your account",
        "password",
        "click here",
        "bank details",
        "account suspended"
    ]

    email_lower = email_text.lower()
    found = []

    for word in suspicious_words:
        if word in email_lower:
            found.append(word)

    if "http://" in email_lower:
        found.append("Unencrypted HTTP link")

    print("\n--- Email Security Report ---")

    if len(found) >= 3:
        risk = "HIGH"
    elif len(found) >= 1:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print("Risk Level:", risk)

    if found:
        print("Warning: Suspicious signs detected!")
        print("Indicators found:", ", ".join(found))
    else:
        print("No listed warning signs detected.")

email = input("Paste a sample email text: ")
check_email(email)
