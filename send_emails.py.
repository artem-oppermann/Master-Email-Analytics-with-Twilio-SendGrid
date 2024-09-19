from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import csv
import os

sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

def send_email(to_email):
    message = Mail(
        from_email='<YOUR EMAIL ADDRESS>',
        to_emails=to_email,
        subject='Explore Twilio SendGrid - Your Email Marketing Solution',
        html_content=(
            '<strong>Boost your email marketing campaigns with Twilio SendGrid!</strong><br>'
            'Experience seamless email delivery, real-time analytics, and more.<br>'
            '<a href="https://sendgrid.com">Click here to register on SendGrid</a>'
        )
    )
    try:
        response = sendgrid_client.send(message)
        if response.status_code != 202:
            raise Exception(f'Failed to send email to {to_email}. Status code: {response.status_code}')
        print(f'Email sent to {to_email} successfully. Status code: {response.status_code}')
    except Exception as e:
        print(f'Error: {str(e)}')

def send_all_emails():
    with open('email_list.csv', newline='') as csvfile:
        email_reader = csv.reader(csvfile)
        for row in email_reader:
            email = row[0]  # assuming email is in the first column
            send_email(email)

if __name__ == '__main__':
    send_all_emails()
