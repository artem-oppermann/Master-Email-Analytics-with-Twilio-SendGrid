# Real-Time SMS Notification System with Twilio SendGrid and Flask

This project is a tutorial for building a real-time SMS notification system that tracks email campaign metrics using **Twilio SendGrid**, **Python**, and **Flask**. You will be able to monitor key email interactions such as deliveries, opens, clicks, and spam reports through SendGrid's Event Webhooks. The system also sends periodic SMS notifications with email campaign statistics using **Twilio's SMS API**.

## Features

- **Send Emails** using Twilio SendGrid
- **Monitor Email Events** (Delivered, Opened, Clicked, Spam Reports) with SendGrid Event Webhooks
- **SMS Notifications** with campaign updates using Twilio SMS API
- **Scheduled Updates** using APScheduler

## Prerequisites

- **Python 3.11** or later
- **SendGrid Account**
- **Twilio Account**
- **Flask** framework and required libraries (listed below)
- **ngrok** (for tunneling local webhook events)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/twilio-sendgrid-sms-notification.git
cd twilio-sendgrid-sms-notification
```

2. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables for **SendGrid** and **Twilio**:

```bash
export SENDGRID_API_KEY='your_sendgrid_api_key'
export TWILIO_ACCOUNT_SID='your_twilio_account_sid'
export TWILIO_AUTH_TOKEN='your_twilio_auth_token'
```

5. Configure **ngrok** to expose your Flask app:

```bash
ngrok http 8080
```

6. Replace placeholders in the code with your **email**, **Twilio phone number**, and **recipient phone number**.

## Running the Application

1. To send emails to your recipients, run the `send_emails.py` script:

```bash
python send_emails.py
```

2. To start tracking email metrics and scheduling SMS updates, run the Flask app:

```bash
python app.py
```

The application will track the email events and send SMS updates every hour.

## Key Files

- `send_emails.py`: Sends marketing emails using SendGrid.
- `app.py`: Flask application that handles incoming event webhooks and sends scheduled SMS updates.
- `requirements.txt`: Python dependencies for the project.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License.

---

Built by **Artem Oppermann**, Lead AI Research Engineer specializing in AI, software, and APIs.

