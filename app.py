import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

with open('Evangelho_do_dia.txt', 'r', encoding='utf-8') as f:
    evangelho_texto = f.read()

with open('historico_wikipedia.txt', 'r', encoding='utf-8') as f:
    wikipedia_texto = f.read()

corpo_final = f"{'Evangelho do dia'},\n{evangelho_texto}\n\n"
corpo_final += f"{'='*30}\n\n"
corpo_final += f"{'Este dia na historia e você sabia?'}\n\n"
corpo_final += f"{'='*30}\n\n"
