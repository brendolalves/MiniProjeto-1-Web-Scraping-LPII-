import requests
from bs4 import BeautifulSoup, Comment

def buscar_evangelho():
    url = "https://www.paulus.com.br/portal/liturgia-diaria/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0'}

    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        conteudo_final = ""

        #comentarios = soup.find_all(string=lambda text: isinstance(text, Comment))

        #for coment in comentarios:
        texto_bruto = soup.get_text(separator="\n")
        if "Evangelho:" in texto_bruto:
            conteudo_final = texto_bruto.split("Evangelho:")[1].split("Palavra da salvação.")[0].split()

        return conteudo_final if conteudo_final else "Não foi possivel localizar o Evangelho"
    except Exception as e:
        return f"Erro na conexão: {e}"
    
resultado = buscar_evangelho()

with open('Evangelho_do_dia.txt', "w", encoding="utf-8") as f:
    f.write("Evangelho do Dia\n\n")
    f.write(' '.join(resultado))
    f.write("\n")
    f.write("Palavra da Salvação\n\n")

print("Finalizado, arquivo Evangelho_do_dia.txt foi gerado")

