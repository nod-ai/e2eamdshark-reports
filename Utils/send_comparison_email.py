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

# Email recipient
mail_list = ["praveen.g2@amd.com"]

msg = MIMEMultipart("alternative")
msg["From"] = "praveen.g2@amd.com"
msg["To"] = ", ".join(mail_list)
msg["Subject"] = f"GPU vs CPU Comparison Report - {date}"

msg.attach(MIMEText(html_content, "html"))

# Send via SMTP
try:
    with smtplib.SMTP("atlsmtp10.amd.com", 25) as server:
        server.starttls()
        server.sendmail(msg["From"], mail_list, msg.as_string())
        print(f"Email sent successfully to {', '.join(mail_list)}")
except Exception as e:
    print(f"Error sending email: {e}")
    sys.exit(1)
