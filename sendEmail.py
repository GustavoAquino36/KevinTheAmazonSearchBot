import smtplib

def sendEmail(email):
    sender = ''
    message = ''
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('username', 'password')
        server.sendmail(sender, email, message)