from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from flask_mail import Message, Mail
from threading import Thread
import os
import sys

app = Flask(__name__)

if ("ORION_EMAIL_USERNAME" not in os.environ or "ORION_EMAIL_PASSWORD" not in os.environ):
    print("Error: Orion's email username and/or password not set in the environment variables.")
    exit(1)

app.config.update(
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get("ORION_EMAIL_USERNAME"),
    MAIL_PASSWORD = os.environ.get("ORION_EMAIL_PASSWORD"),
    UPLOAD_FOLDER = "/var/www/static/assets/"
)

mail = Mail(app)

if (not os.path.exists(app.config['UPLOAD_FOLDER'])):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def sendAsyncMail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            print(e)
            return str(e)

# The only two routes we need, no backend/frontend intergration needed
@app.route("/serve", methods=['GET'])
def serve_file():
    return send_from_directory(app.config["UPLOAD_FOLDER"], "stevenShenResume.pdf")

@app.route("/send", methods=['POST'])
def send_email():
    data = request.get_json()['message']

    message = Message(
        'A Message From Orion', 
        sender=app.config['MAIL_USERNAME'],
        recipients=["stevenshen1999@hotmail.com"]
    )

    message.body = f"""\
Hello Steven,\n\nA message from Orion from {data['name']}({data['email']}):\n{data['payload']}\n\n"""

    '''
    try:
        Thread(target=sendAsyncMail, args=(app, message)).start()
    except:
        return jsonfi({'status': 'failed', 'message': 'Email server misconfigured or unavaliable'})
    '''
    try:
        mail.send(message)
    except:
        return jsonify({'status': 'failure'}), 400

    return jsonify({'status': 'success'})

CORS(app)

if __name__ == "__main__":
    app.run()
