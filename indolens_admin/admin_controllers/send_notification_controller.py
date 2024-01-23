import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def send_email(subject, body, to_email):
    # smtp_server = "smtppro.zoho.in"
    # smtp_port = 465  # This might vary, check with your email provider
    # smtp_username = "santhoshkumar@accelstack.in"
    # smtp_password = "BJyZHHA4DeWr"
    #
    # # Create the MIME object
    # msg = MIMEMultipart()
    # msg['From'] = smtp_username
    # msg['To'] = to_email
    # msg['Subject'] = subject
    #
    # # Attach the email body as plain text
    # msg.attach(MIMEText(body, 'plain'))
    #
    # # Connect to the SMTP server
    # with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    #     server.login(smtp_username, smtp_password)
    #     server.sendmail(smtp_username, to_email, msg.as_string())
    #
    # print("Email sent successfully.")

    url = 'https://api.emailjs.com/api/v1.0/email/send'
    data = {
        'service_id': 'service_7eqv3fu',
        'template_id': 'template_1c47e6b',
        'user_id': 'qbWAgwqHOFbcgoJRF',
        'template_params': {
            'to_email': to_email,
            'subject': subject,
            'body': body,
            'g-recaptcha-response': '03AHJ_ASjnLA214KSNKFJAK12sfKASfehbmfd...'
        }
    }

    headers = {'Content-Type': 'application/json'}

    email_response = requests.post(url, data=json.dumps(data), headers=headers)
    return email_response