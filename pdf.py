import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader
import os
import re

def gerar_projeto():

    savegnago_url = "https://imagens.savegnagoonline.com.br/jornal-semanal-app/Rio_Claro.pdf"
    res_pdf = requests.get(savegnago_url, headers={'User-Agent': 'Mozilla/5.0'})
    with open("temp_savegnago.pdf", "wb") as f:
        f.write(res_pdf.content)
    print(f"✓ PDF baixado com sucesso! Tamanho: {len(res_pdf.content)} bytes")
    print(f"✓ Arquivo salvo como: temp_savegnago.pdf")

if __name__ == "__main__":
    gerar_projeto()
