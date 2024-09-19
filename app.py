from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

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
