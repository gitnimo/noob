import email.message
msg=email.message.EmailMessage()
msg["From"]="e9w9a3n611@gmail.com"
msg["to"]="e9w9a3n611@yahoo.com.tw"
msg["subject"]="你好，我是nimo"
msg.set_content("OMGOMG")

import smtplib

sever=smtplib.SMTP_SSL("smtp.gmail.com",465)
sever.login("e9w9a3n611@gmail.com","e2w1a0n584")
sever.send_message(msg)
sever.close () 
 #寄信code

