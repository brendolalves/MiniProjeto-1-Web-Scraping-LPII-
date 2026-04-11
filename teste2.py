import requests
from bs4 import BeautifulSoup

def buscar_dados():
    relatorio = "--- RELATÓRIO DO DIA ---\n\n"
    headers = {'User-Agent': 'Mozilla/5.0'}

    # 1. Wikipédia (Ajustado para ser mais flexível)
    try:
        res_wiki = requests.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal", headers=headers)
        soup_wiki = BeautifulSoup(res_wiki.text, 'html.parser')
        
        # Tentamos pelo ID, se falhar, buscamos pela classe da seção informativa
        neste_dia = soup_wiki.find(id="main-itd") or soup_wiki.select_one(".main-block.eventos")
        
        if neste_dia:
            relatorio += "NESTE DIA NA HISTÓRIA:\n" + neste_dia.get_text(separator=" ").strip() + "\n\n"
        else:
            relatorio += "Aviso: Seção 'Neste Dia' mudou de lugar na Wikipédia.\n\n"
    except Exception as e:
        relatorio += f"Erro técnico na Wikipédia: {e}\n\n"

    # 2. Canção Nova (Ajustado para pegar o conteúdo principal)
    try:
        res_cn = requests.get("https://liturgia.cancaonova.com/pb/", headers=headers)
        soup_cn = BeautifulSoup(res_cn.text, 'html.parser')
        
        # Buscamos a div que contém toda a liturgia
        conteudo = soup_cn.find('div', class_='content-liturgia') or soup_cn.find('article')
        
        if conteudo:
            texto_bruto = conteudo.get_text(separator="\n")
            # Procuramos onde começa o Evangelho e cortamos o resto
            if "Evangelho" in texto_bruto:
                parte_evangelho = texto_bruto.split("Evangelho")[-1]
                # Limpa o texto tirando espaços excessivos
                relatorio += "EVANGELHO DO DIA:\n" + parte_evangelho.strip() + "\n\n"
            else:
                relatorio += "Aviso: Palavra 'Evangelho' não encontrada na liturgia de hoje.\n\n"
        else:
            relatorio += "Aviso: Não foi possível localizar o bloco de liturgia na Canção Nova.\n\n"
    except Exception as e:
        relatorio += f"Erro técnico na Canção Nova: {e}\n\n"

    # 3. Savegnago (Link direto)
    relatorio += "OFERTAS SAVEGNAGO RIO CLARO:\n"
    relatorio += "https://imagens.savegnagoonline.com.br/jornal-semanal-app/Rio_Claro.pdf"

    return relatorio

# Execução e gravação
try:
    conteudo_final = buscar_dados()
    with open("meu_relatorio.txt", "w", encoding="utf-8") as f:
        f.write(conteudo_final)
    print("Sucesso! Verifique o arquivo 'meu_relatorio.txt'.")
except Exception as e:
    print(f"Erro ao salvar arquivo: {e}")