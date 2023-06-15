import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('cherukuriumadevi09@gmail.com','whkbnisbnsxjwoul')
    msg=EmailMessage()
    msg['From']='cherukuriumadevi09@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()