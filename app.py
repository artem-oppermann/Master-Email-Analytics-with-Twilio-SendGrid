import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///email_events.db'
db = SQLAlchemy(app)

class EmailEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(50))
    email = db.Column(db.String(255))

with app.app_context():
    db.create_all()

@app.route('/event', methods=['POST'])
def event():
    data = request.get_json(force=True)
    for event_data in data:
        email_event = EmailEvent(event=event_data['event'], email=event_data['email'])
        db.session.add(email_event)
    db.session.commit()
    return jsonify({'status': 'success'}), 200

# Twilio credentials
account_sid = 'your_twilio_account_sid_here'
auth_token = 'your_twilio_auth_token_here'
client = Client(account_sid, auth_token)

def send_sms_update():
    with app.app_context():
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        total_emails = EmailEvent.query.count()
        delivered = EmailEvent.query.filter_by(event='delivered').count()
        opened = EmailEvent.query.filter_by(event='open').count()
        clicked = EmailEvent.query.filter_by(event='click').count()
        spamreports = EmailEvent.query.filter_by(event='spamreport').count()

        if total_emails > 0:
            delivered_perc = (delivered / total_emails) * 100
            opened_perc = (opened / delivered_perc) * 100
            clicked_perc = (clicked / delivered_perc) * 100
            spamreports_perc = (spamreports / delivered_perc) * 100
        else:
            delivered_perc = opened_perc = clicked_perc = spamreports_perc = 0

        message_body = (
            f"Email Campaign Stats as of {current_datetime}:\n"  
            f"Total Emails: {total_emails}\n"
            f"Delivered: {delivered} ({delivered_perc:.2f}%)\n"
            f"Opened: {opened} ({opened_perc:.2f}%)\n"
            f"Clicked: {clicked} ({clicked_perc:.2f}%)\n"
            f"Marked as Spam: {spamreports} ({spamreports_perc:.2f}%)"
        )

        sms_message = client.messages.create(
            body=message_body,
            from_='your_twilio_phone_number',
            to='phone_number_to_send_sms_to'
        )

        print(f'SMS sent with ID {sms_message.sid}')

def schedule_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_sms_update, 'interval', minutes=60)
    scheduler.start()

if __name__ == '__main__':
    schedule_jobs()
    app.run(port=8080, debug=False)


