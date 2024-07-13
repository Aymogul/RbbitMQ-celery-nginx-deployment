from flask import Flask, request
from datetime import datetime
import logging
from tasks import send_email

app = Flask(__name__)

logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

@app.route('/endpoint')
def endpoint():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email.delay(sendmail)
        return f"Email to {sendmail} queued."

    if talktome:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Current time logged: {now}")
        return "Current time logged."

    return "No action performed."

if __name__ == '__main__':
    app.run(debug=True)