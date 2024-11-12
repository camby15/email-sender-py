import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from python!"
body = "This is a test emailfrom pyhton"
sender_email = "akambay2k@gmail.com"       """add any emaill at any time """
receiver_email = "omorimbaram@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    sever.login(sender_email, password)
    sever.sendmail(sender_email, receiver_email, message.as_string())
    
print("succes")