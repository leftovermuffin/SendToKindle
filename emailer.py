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
	
	def sendToKindle(self, filename):
		fromaddr = "higloomybunny@gmail.com"
		# toaddr = "higloomybunny@kindle.com"
		toaddr = "meparthaprotim@gmail.com"
		print('--- sending mail from ' + fromaddr + ' to ' + toaddr + ' ---')
		
		# meta information
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Python email"


		part = MIMEBase('application', "octet-stream")
		with open(filename, 'rb') as file:
		    part.set_payload(file.read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition',
		                'attachment; filename="{}"'.format(op.basename(filename)))
		msg.attach(part)

		print('--- file attached --- ')

		auth_email = ""
		auth_pass = ""

		with open('auth.txt') as authfile:
			data = json.load(authfile)
			auth_email = data['email']
			auth_pass = data['pass']

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(auth_email, auth_pass)

		
		text = msg.as_string()
		# server.sendmail(fromaddr, toaddr, text)

		print('--- mail sent! ---')

