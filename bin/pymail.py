
from helper import *

def main():

	sender_mail_id, password = get_sender_mail_id_password()
	receiver_mail_id_list = get_receiver_mail_id_list()

	# instance of MIMEMultipart 
	obj = MIMEMultipart()

	# storing the senders email address  
	obj['From'] = sender_mail_id
	
	# storing the receivers email address  
	obj['To'] = reciver_mai_id_list[0] 
  
	# storing the subject
	obj['Subject'] = get_subject()
  
	# string to store the body of the mail 
	body = get_body()

	# attach the body with the msg instance 
	obj.attach(MIMEText(body, 'plain'))

	# open the file to be sent  
	print("Enter file name (with extension): ")
	filename = input()
	attachment = open(filename, "rb")

	# instance of MIMEBase and named as p 
	obj2 = MIMEBase('application', 'octet-stream') 
  
	# To change the payload into encoded form 
	obj2.set_payload((attachment).read()) 
  
	# encode into base64 
	encoders.encode_base64(obj2) 
   
	obj2.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
	# attach the instance 'p' to instance 'msg' 
	obj.attach(obj2)

	send_mail(obj, obj2)

if __name__ == '__main__':
	main()
