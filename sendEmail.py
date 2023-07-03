import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def stringfyMessage(lista, shorturl, title, fullPrice, seller):
    mediaValores = sum(lista) / len(lista)
    return (
        f'''Média dos preços: R$ {str(mediaValores).replace('.', ',')}\n
        Item mais barato:
        URL do Site: {shorturl}
        Nome do Item encontrado: {title}
        Preço do item: R$ {fullPrice.replace('.', ',')}
        Vendido por: {seller}
    ''')

def sendEmail(message, receiver):
    sender = 'amazonresearchbot@gmail.com'

    email = MIMEMultipart()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = 'Subject test'
    email.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('amazonresearchbot@gmail.com', 'ehnzknbniorxxvpf')
        server.sendmail(email['From'], email['To'], email.as_string())
        server.quit()