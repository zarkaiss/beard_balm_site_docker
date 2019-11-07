from flask_mail import Message
from app import mail
from flask import render_template, current_app, url_for
import os
import boto3
from itsdangerous import URLSafeTimedSerializer


#def send_email(subject, sender, recipients, text_body, html_body):
   # msg = Message(subject, sender=sender, recipients=recipients)
  #  msg.body = text_body
 #   msg.html = html_body
#    mail.send(msg)


def send_password_reset_email(email):
    password_reset_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    
    password_reset_url = url_for('main.reset_with_token', token=password_reset_serializer.dumps(
        email, salt='password-reset-salt'), _external=True)
        
    html = render_template('email/reset_password.txt', password_reset_url=password_reset_url)
    
    ses = boto3.client(
        'ses',
        region_name=os.getenv('SES_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    ses.send_email(
        Source= os.getenv('SES_EMAIL_SOURCE'),
        Destination={'ToAddresses': [email]},
        Message = {
            'Subject': {'Data': 'Reset Your Password'},
            'Body': {
                'Text': {'Data': html}
            }
                
        }
    )
    
    
    #send_email('[Beard Brothers] Reset Your Password',
     #       sender = current_app.config['ADMINS'][0],
      #      recipients=[user.email],
        #    text_body=render_template('email/reset_password.txt',user=user, token=token),
        #    html_body=render_template('email/reset_password.html', user=user, token=token))

