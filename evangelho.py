import requests
from bs4 import BeautifulSoup


class Evangelho:
    def __init__(self):
        self.url = "https://www.paulus.com.br/portal/liturgia-diaria/"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0'}

    def obter_dados(self):
        try:
            res = requests.get(self.url, headers=self.headers)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')
            conteudo_final = ""
            texto_bruto = soup.get_text(separator="\n")
            
            if "Evangelho:" in texto_bruto:
                conteudo_final = texto_bruto.split("Evangelho:")[1].split("Palavra da salvação.")[0].split()

                return conteudo_final if conteudo_final else "Não foi possivel localizar o Evangelho"
        except Exception as e:
            return f"Erro na conexão: {e}"

evangelho = Evangelho()
resultado = evangelho.obter_dados()

with open('Evangelho_do_dia.txt', "w", encoding="utf-8") as f:
    f.write("Evangelho do Dia\n\n")
    f.write(' '.join(resultado) if isinstance(resultado, list) else resultado)
    f.write("\n")
    f.write("Palavra da Salvação\n\n")

print("Finalizado, arquivo Evangelho_do_dia.txt foi gerado")

