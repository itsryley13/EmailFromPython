import smtplib
import time
print("Welcome To The Python Email Sender!")

emailserver=input("Choose a)Gmail b)OutLook")


if emailserver == "a":


	sendersemail=input("Enter YOUR Gmail:\n")
	senderspass=input("Enter YOUR Password:\n")
	content=input("Enter What The Email Will Say:\n")
	emailto=input("Enter The Gmail Of The Person You Are Sending To:\n")
	mail = smtplib.SMTP("smtp.gmail.com",587)
	mail.ehlo()
	mail.starttls()
	mail.login(sendersemail,senderspass)
	mail.sendmail(sendersemail,emailto,content)
	mail.close()


	print("Sending Email...")
	time.sleep(5)
	print("Email Sent")




elif emailserver == "b":
	 


	sendersemail=input("Enter YOUR Hotmail:\n")
	senderspass=input("Enter YOUR Password:\n")
	content=input("Enter What The Email Will Say:\n")
	emailto=input("Enter The Hotmail Of The Person You Are Sending To:\n")
	mail = smtplib.SMTP("smtp.live.com",25)
	mail.ehlo()
	mail.starttls()
	mail.login(sendersemail,senderspass)
	mail.sendmail(sendersemail,emailto,content)
	mail.close()

	print("Sending Email...")
	time.sleep(5)
	print("Email Sent")
