#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: send_comparison_email.py <html_file_path>")
    sys.exit(1)

date = datetime.today().strftime('%Y-%m-%d')

html_file_path = Path(sys.argv[1])

if not html_file_path.exists():
    print(f"Error: HTML file not found: {html_file_path}")
    sys.exit(1)

with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Read email list from file
email_list_path = Path(__file__).with_name('email_list.txt')
if not email_list_path.exists():
    print(f"Error: Email list file not found: {email_list_path}")
    sys.exit(1)

with email_list_path.open('r') as f:
    mail_list = [email.strip() for email in f.read().splitlines() if email.strip()]

msg = MIMEMultipart("alternative")
msg["From"] = "praveen.g2@amd.com"
msg["To"] = ", ".join(mail_list)
msg["Cc"] = "praveen.g2@amd.com"
msg["Subject"] = f"ONNX Reports Summary - {date}"

msg.attach(MIMEText(html_content, "html"))

# Send via SMTP (include CC in recipients)
all_recipients = mail_list + [msg["Cc"]]
try:
    with smtplib.SMTP("atlsmtp10.amd.com", 25) as server:
        server.starttls()
        server.sendmail(msg["From"], all_recipients, msg.as_string())
        print(f"Email sent successfully to {', '.join(mail_list)} (CC: {msg['Cc']})")
except Exception as e:
    print(f"Error sending email: {e}")
    sys.exit(1)
