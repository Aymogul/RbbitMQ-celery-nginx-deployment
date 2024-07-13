from celery import Celery
import smtplib
from email.mime.text import MIMEText

celery = Celery('tasks')
celery.config_from_object('celeryconfig')

@celery.task
def send_email(to_email):
    from_email = 'your-email@gmail.com'
    password = 'your-email-password'

    msg = MIMEText("This is a test email.")
    msg['Subject'] = 'Test Email'
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())