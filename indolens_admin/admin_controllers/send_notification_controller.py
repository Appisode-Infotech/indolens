import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

from indolens_admin.admin_controllers.admin_setting_controller import get_admin_setting, get_emailjs_attribute


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

    emailjs = get_emailjs_attribute()
    if any(emailjs.values()):
        print(emailjs.get('emailjs_url'))
        print(emailjs.get('emailjs_template_id'))
        print(emailjs.get('emailjs_user_id'))
        print(emailjs.get('emailjs_recaptcha'))

        url = emailjs.get('emailjs_url')
        data = {
            'service_id': emailjs.get('emailjs_service_id'),
            'template_id': emailjs.get('emailjs_template_id'),
            'user_id': emailjs.get('emailjs_user_id'),
            'template_params': {
                'to_email': to_email,
                'subject': subject,
                'body': body,
                'g-recaptcha-response': emailjs.get('emailjs_recaptcha')
            }
        }

        headers = {'Content-Type': 'application/json'}

        email_response = requests.post(url, data=json.dumps(data), headers=headers)
        print(email_response)
        return email_response
    else:
        print("Data is empty")
        return "no email js credentials found"


