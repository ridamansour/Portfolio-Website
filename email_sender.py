import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def email_send(email_sender, subject_sender, email_content):
    try:
        email = EmailMessage()
        email['from'] = email_sender
        email['to'] = 'ridamansour111@gmail.com'
        email['subject'] = subject_sender
        email.set_content(f'this is from {email_sender} \n\n{email_content} ')
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('ridamansour1111@gmail.com', os.getenv("EMAIL_PASS"))
            smtp.send_message(email)
            return 'email is sent'
    except Exception:
        print(Exception)
    return 0