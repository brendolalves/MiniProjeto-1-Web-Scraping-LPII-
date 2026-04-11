import requests
from bs4 import BeautifulSoup, Comment

def buscar_neste_dia():
    url = "https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0'}
    
    try:
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        conteudo_final = ""

        # ESTRATÉGIA 1: Buscar pelos comentários HTML (Sua ideia)
        comentarios = soup.find_all(string=lambda text: isinstance(text, Comment))
        for coment in comentarios:
            if "NESTE DIA" in coment.upper() and "INÍCIO" in coment.upper():
                # Pegamos o elemento pai ou o próximo elemento para extrair o texto
                secao = coment.find_parent()
                if secao:
                    conteudo_final = secao.get_text(separator=" ").strip()
                    break

        # ESTRATÉGIA 2: Caso a 1 falhe, busca pelo ID padrão da Wikipédia
        if not conteudo_final:
            bloco = soup.find(id="main-itd")
            if bloco:
                conteudo_final = bloco.get_text(separator=" ").strip()

        # ESTRATÉGIA 3: Busca bruta por texto (Último recurso)
        if not conteudo_final:
            texto_bruto = soup.get_text(separator="\n")
            if "Neste dia" in texto_bruto:
                conteudo_final = texto_bruto.split("Neste dia")[1].split("Ver mais")[0].strip()

        return conteudo_final if conteudo_final else "Não foi possível localizar a seção 'Neste dia'."

    except Exception as e:
        return f"Erro na conexão: {e}"

# --- EXECUÇÃO ---
resultado = buscar_neste_dia()

# Salvando no arquivo .txt
with open("historico_wikipedia.txt", "w", encoding="utf-8") as f:
    f.write("=== EVENTOS HISTÓRICOS DE HOJE ===\n\n")
    f.write(resultado)

print("Projeto finalizado! O arquivo 'historico_wikipedia.txt' foi gerado.")