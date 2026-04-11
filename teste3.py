import requests
from bs4 import BeautifulSoup, Comment

def buscar_wikipedia_por_comentario():
    url = "https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # 1. Localizar todos os comentários no HTML
        comentarios = soup.find_all(string=lambda text: isinstance(text, Comment))

        conteudo_filtrado = ""
        capturando = False

        # 2. Iterar pelos elementos do HTML para pegar o que está entre os comentários
        # Vamos procurar pelo comentário que contém "NESTE DIA" e "INÍCIO"
        for coment in comentarios:
            if "NESTE DIA" in coment and "INÍCIO" in coment:
                # Encontramos o ponto de partida! 
                # Agora vamos pegar os elementos irmãos (siblings) até chegar no fim
                proximo_elemento = coment.parent.next_sibling
                
                while proximo_elemento:
                    # Se encontrarmos o comentário de FIM, paramos
                    if isinstance(proximo_elemento, Comment) and "FIM" in proximo_elemento:
                        break
                    
                    # Se for um elemento com texto, acumulamos
                    if hasattr(proximo_elemento, 'get_text'):
                        conteudo_filtrado += proximo_elemento.get_text(separator=" ").strip() + "\n"
                    
                    proximo_elemento = proximo_elemento.next_sibling
                break

        return conteudo_filtrado if conteudo_filtrado else "Comentário não encontrado."

    except Exception as e:
        return f"Erro técnico: {e}"

# Teste rápido
texto = buscar_wikipedia_por_comentario()
print("--- CONTEÚDO CAPTURADO VIA COMENTÁRIOS ---")
print(texto)