
import tkinter as tk
from tkinter import scrolledtext, filedialog


def analyze_email():
    email = email_box.get("1.0", tk.END).strip().lower()

    suspicious_words = [
        "urgent",
        "verify your account",
        "password",
        "click here",
        "bank details",
        "account suspended"
    ]

    found = [word for word in suspicious_words if word in email]

    if "http://" in email:
        found.append("Unencrypted HTTP link")

    if len(found) >= 3:
        risk = "HIGH"
    elif len(found) >= 1:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    report = f"Risk Level: {risk}\n\n"

    if found:
        report += "Warning signs:\n- " + "\n- ".join(found)
    else:
        report += "No listed warning signs found."

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, report)
    result_box.config(state="disabled")

    save_button.config(state="normal")


def save_report():
    report = result_box.get("1.0", tk.END).strip()

    if not report:
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Security Report"
    )

    if path:
        with open(path, "w", encoding="utf-8") as file:
            file.write(report)


window = tk.Tk()
window.title("Phishing Email Detector")
window.geometry("600x520")

tk.Label(
    window,
    text="Phishing Email Detector",
    font=("Arial", 20, "bold")
).pack(pady=15)

tk.Label(window, text="Paste email text below:").pack()

email_box = scrolledtext.ScrolledText(
    window, width=65, height=10
)
email_box.pack(padx=15, pady=10)

tk.Button(
    window,
    text="Analyze Email",
    command=analyze_email
).pack(pady=10)

save_button = tk.Button(
    window,
    text="Save Report",
    command=save_report,
    state="disabled"
)
save_button.pack(pady=5)

result_box = scrolledtext.ScrolledText(
    window, width=65, height=8, state="disabled"
)
result_box.pack(padx=15, pady=10)

window.mainloop()