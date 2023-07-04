import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from lerXLSX import LerConfig

config = LerConfig()

def stringfyMessage(item, lista, shorturl, title, fullPrice, seller):
    mediaValores = sum(lista) / len(lista)
    mediaValores = '{:.2f}'.format(mediaValores)
    return (
        f'''
<div style="
border: 1px solid black; 
width: fit-content; 
padding: 15px; 
border-radius: 5px;
">
<header>
Item pesquisado: {item} <br>
Média dos preços: R$ {str(mediaValores).replace('.', ',')} 
</header> <br>
<b>Item mais barato:</b>
<ul>
    <li>URL do Site: {shorturl}</li>
    <li>Nome do Item encontrado: {title}</li>
    <li>Preço do item: R$ {str(fullPrice).replace('.', ',')}</li>
    <li>Vendido por: {seller}</li>
</ul>
</div>
''')


def sendEmail(message, receiver):
    sender = 'amazonresearchbot@gmail.com'

    email = MIMEMultipart()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = 'Subject test'
    email.attach(MIMEText(message, 'html'))
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, config['senha'])
        server.sendmail(email['From'], email['To'], email.as_string())
        server.quit()