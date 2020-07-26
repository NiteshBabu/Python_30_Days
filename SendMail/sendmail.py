import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()


import os

username = 'chromastonebigchill@gmail.com'
password = os.environ.get('mail_password')
from_email = 'chromastonebigchill'
# to_emails = 'niteshbabusharma@gmail.com'

def send_mail(from_email=' NickK <chromastonebigchill@gmail.com>', to_emails=[], body=None, subject=None, body_type='plain'):
	message = MIMEMultipart()
	message['From'] = from_email
	message['To'] = ",".join(to_emails)
	message['Subject'] = subject
	if body_type == 'html':
		message.attach(MIMEText(body, 'html')) 
	elif body_type == 'text':
		message.attach(MIMEText(body, 'plain')) 
	
	text = message.as_string()

	server = smtplib.SMTP(host='smtp.gmail.com', port=587)
	server.ehlo()
	server.starttls()
	server.login(username, password)
	server.sendmail(from_email, to_emails, text)
	server.quit()
	print('Sent Successfully')

send_mail(to_emails=['<niteshbabusharma@gmail.com>','chromastonebigchill@gmail.com'],body="<h1 style='color:pink;'>Nitesh Babu => Python</h1>", subject="Subject", body_type='html')
