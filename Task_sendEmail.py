# This is the module which we will use for sending the mails without using a gmail
import smtplib

# defining a function which will use for sending Mails


def SenMail(sender_mail, sender_password, receiver_mail, subject):
    # Linking to gmail server by passing port number
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_mail, sender_password)
    server.sendmail(sender_mail, receiver_mail, subject)


# Taking input from user as Sender mail, Sender Password, Receiver Email id and the content that yoy want to send
sender_mail = input("Enter the Email ID of Sender: ")
receiver_mail = input("Enter the Email ID of Receiver: ")
password = input("Enter the Password of the Sender Email ID: ")
content = input("Enter the subject that you want to send: ")

try:
    SenMail(sender_mail, password, receiver_mail, content)  # Calling function
    print("Mail Has Been Succeesfully Send!")

except Exception as e:
    print("Sorry, I am not able to send this email")
