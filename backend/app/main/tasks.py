import time
import os
import boto3
from app import db
from flask_mail import Message
from app import mail
from flask import current_app
from app.models import User


def send_email(email, body):
   # time.sleep(10)
    ses = boto3.client(
            'ses',
            region_name=os.getenv('SES_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    ses.send_email(
            Source = os.getenv('SES_EMAIL_SOURCE'),
            Destination={'ToAddresses': [email]},
            Message = {
                'Subject': {'Data': 'Confirm Your Account'},
                'Body': {
                    'Text': {'Data': body}
                }
            }
        )
    user = User.query.filter_by(email=email).first()
    user.email_sent = True
    db.session.commit()
    return True



