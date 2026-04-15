import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

hoje = datetime.now()
data = hoje.strftime("%d/%m/%Y")

with open('Evangelho_do_dia.txt', 'r', encoding='utf-8') as f:
    evangelho_texto = f.read()

with open('historico_wikipedia.txt', 'r', encoding='utf-8') as f:
    wikipedia_texto = f.read()

corpo_final = f"{'Evangelho do dia ', data},\n{evangelho_texto}\n\n"
corpo_final += f"{'='*30}\n\n"
corpo_final += f"{'Este dia na história e você sabia?'}, \n{wikipedia_texto}\n\n"
corpo_final += f"{'='*30}\n\n"
corpo_final += f"Veja as oferta do dia {' ', data} do supermercado Savegnago"

msg = EmailMessage()
msg['Subject'] = "Seu relatório diário"
msg['From'] = EMAIL_USER
destinatario = input('Digite o endereço de email do destinatário: ')
msg['To'] = destinatario
msg.set_content(corpo_final)

ofertas = 'ofertas.pdf'
with open(ofertas, 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype = 'application',
        subtype='pdf',
        filename=os.path.basename(ofertas)
    )

try: 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
    print('Email enviado com sucesso')
except Exception as e:
    print(f'Erro ao enviar: {e}')