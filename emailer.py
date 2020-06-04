from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders
import os.path as op
import logging
import json


class GloomyEmailer:
	
	def sendToKindle(self, thefilename):
		auth_email = ""
		auth_pass = ""
		kindle_mail = ""
		with open('auth.txt') as authfile:
			data = json.load(authfile)
			auth_email = data['email']
			auth_pass = data['pass']
			kindle_mail = data['kindleMail']

		# fromaddr = "higloomybunny@gmail.com"
		# toaddr = kindle_mail
		# toaddr = "meparthaprotim@gmail.com"
		print('--- sending mail from ' + auth_email + ' to ' + kindle_mail + ' ---')
		
		# meta information
		msg = MIMEMultipart()
		msg['From'] = auth_email
		msg['To'] = kindle_mail
		msg['Subject'] = "Python email"


		part = MIMEBase('application', "octet-stream")
		with open(thefilename, 'rb') as file:
		    part.set_payload(file.read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition',
		                'attachment; filename="{}"'.format(op.basename(thefilename)))
		msg.attach(part)

		print('--- file attached --- ')

		

		

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(auth_email, auth_pass)

		
		text = msg.as_string()
		server.sendmail(auth_email, kindle_mail, text)

		print('--- mail sent! ---')

