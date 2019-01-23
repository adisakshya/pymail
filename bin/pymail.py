import email, smtplib, ssl
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_sender_details():

	return sys.argv[1], sys.argv[2]

def get_receiver_email_list():

	receivers_list = []

	while True:

		receiver_email = input('Enter Reveiver Email: ')
		receivers_list.append(receiver_email)
		print('Receivers List: ', receivers_list)

		if input('Want to add more receivers? (Y/N): ') in ['n', 'N']:

			break

	return receivers_list		

def main():

	sender_email, password = get_sender_details()
	receivers_email_list = get_receiver_email_list()
	subject = input('Enter Subject: ')
	body = input('Enter Body: ')

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["Subject"] = subject
	#filename = "github.pdf"  # In same directory as script

	for i in range(len(receivers_email_list)):

		message["To"] = receivers_email_list[i]
		
		# Add body to email
		message.attach(MIMEText(body, "plain"))

		if input('Any attachments?(Y/N): ') in ['y', 'Y']:
			
			filename = input('Enter filename for attachments: ')
			with open(filename, 'rb') as attachment:
				part = MIMEBase("application","octet-stream")
				part.set_payload(attachment.read())

			# Add header as key/value pair to attachment part
			part.add_header(
    			"Content-Disposition",
    			f"attachment; filename= {filename}",
			)

		# Add attachment to message and convert message to string
		message.attach(part)
		text = message.as_string()

		# Log in to server using secure context and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receivers_email_list[i], text)
			print("Email sent to: ", receivers_email_list[i])

if __name__ == '__main__':
	main()
