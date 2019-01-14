
def get_sender_mail_id_password():

	print("Enter E-mail ID: ")
	mail_id = input()
	print("Enter Password: ")
	password = input()

	return [mail_id, password]

def get_rceiver_mail_id_list():

	receivers_list = []
	response = 'y'
	i = 1
	while response in ['y', 'Y']:

		print("Enter E-mail ID of Receiver ",i)
		i = i + 1
		mail_id = input()
		receivers_list.append(mail_id)
		print("Want to add more recievers? (Y/N): ")
		response = input()

	return receivers_list	

def get_subject():

	print("Enter Subject: ")
	subject = input()
	if len(subject) != 0:
		return subject
	else:
		return 'Sent from pymail'	

def get_body():

	print("Input body: ")
	body = input()
	return body

def send_mail(obj, sender_mail_id, password, receiver_mail_id_list):

	try:

		for i in range(len(receiver_mail_id_list)):
			# creates SMTP session 
			s = smtplib.SMTP(sender_mail_id, 587) 
  
			# start TLS for security 
			s.starttls() 
  
			# Authentication 
			s.login(sender_mail_id, password) 
  
			# Converts the Multipart msg into a string 
			text = obj.as_string() 
  
			# sending the mail 
			s.sendmail(sender_mail_id, receiver_mail_id_list[0], text) 
  
			# terminating the session 
			s.quit()
			
	except Exception as error:
		print('Caught error: ' + repr(error)) 	 
