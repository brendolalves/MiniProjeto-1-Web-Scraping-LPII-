import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader
import os
import re

# --- CLASSE PARA O PDF DE TEXTO ---
class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "RELATÓRIO DIÁRIO INTEGRADO", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(3)

    def section_body(self, body):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, body)
        self.ln(5)

def buscar_dados():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    # Wikipédia
    res_wiki = requests.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal", timeout=10, headers=headers)
    soup = BeautifulSoup(res_wiki.text, 'html.parser')
    section = soup.find('h2', string=re.compile(r'abril'))
    if section:
        ul = section.find_next('ul')
        if ul:
            wiki_txt = ul.get_text(separator="\n").strip()
        else:
            wiki_txt = "UL não encontrada."
    else:
        wiki_txt = "Seção não encontrada."

    # Canção Nova
    res_cn = requests.get("https://liturgia.cancaonova.com/pb/", timeout=10, headers=headers)
    soup_cn = BeautifulSoup(res_cn.text, 'html.parser')
    full_text = soup_cn.get_text()
    if "Evangelho" in full_text:
        evangelho_part = full_text.split("Evangelho")[-1].split("Palavra do Senhor")[0].strip()
        evangelho_txt = evangelho_part + "\n- Palavra da Salvação"
    else:
        evangelho_txt = "Evangelho não encontrado."
    
    return wiki_txt, evangelho_txt

def gerar_projeto():
    # 1. Buscar Textos
    txt_wiki, txt_eva = buscar_dados()

    # Replace Unicode characters that fpdf can't handle
    txt_wiki = txt_wiki.replace("—", "-").replace("–", "-").encode('latin-1', 'ignore').decode('latin-1')
    txt_eva = txt_eva.replace("—", "-").replace("–", "-").encode('latin-1', 'ignore').decode('latin-1')

    # 2. Criar o PDF temporário com os textos
    pdf_texto = PDF()
    pdf_texto.add_page()
    pdf_texto.section_title("EVANGELHO DO DIA")
    pdf_texto.section_body(txt_eva)
    pdf_texto.section_title("ACONTECIMENTOS NESTE DIA")
    pdf_texto.section_body(txt_wiki)
    pdf_texto.output("temp_textos.pdf")

    # 3. Baixar o PDF do Savegnago
    savegnago_url = "https://imagens.savegnagoonline.com.br/jornal-semanal-app/Rio_Claro.pdf"
    res_pdf = requests.get(savegnago_url, headers={'User-Agent': 'Mozilla/5.0'})
    with open("temp_savegnago.pdf", "wb") as f:
        f.write(res_pdf.content)

    # 4. Mesclar os dois PDFs
    merger = PdfWriter()

    # Adiciona as páginas de texto
    for page in PdfReader("temp_textos.pdf").pages:
        merger.add_page(page)

    # Adiciona as páginas do Savegnago
    for page in PdfReader("temp_savegnago.pdf").pages:
        merger.add_page(page)

    # Salva o arquivo final
    with open("Relatorio_Completo_Final.pdf", "wb") as f:
        merger.write(f)

    # 5. Limpar arquivos temporários
    os.remove("temp_textos.pdf")
    os.remove("temp_savegnago.pdf")
    
    print("Sucesso! O arquivo 'Relatorio_Completo_Final.pdf' está pronto.")

if __name__ == "__main__":
    gerar_projeto()