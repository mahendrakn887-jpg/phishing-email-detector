# Phishing Email Detector

A beginner-friendly Python cybersecurity project that identifies suspicious email indicators and assigns a basic risk level.

## Features

* Detects suspicious keywords such as "urgent" and "verify your account"
* Identifies unencrypted HTTP links
* Assigns LOW, MEDIUM, or HIGH risk levels
* Provides a graphical interface using Tkinter
* Saves security analysis reports as text files

## Technologies Used

* Python 3
* Tkinter
* Visual Studio Code

## How to Run

1. Install Python 3.

2. Download or clone this repository.

3. Open a terminal in the project folder.

4. Run the graphical application:

   `python app.py`

5. Paste sample email text and click **Analyze Email**.

To run the terminal version instead:

`python detector.py`

## Limitations

This project uses basic keyword matching and HTTP link detection. It cannot confirm whether an email is genuinely malicious or safe. HTTPS links can also be malicious.

## Learning Goals

This project demonstrates beginner Python programming, basic phishing awareness, simple risk classification, and report generation.
