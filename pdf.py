import requests

class folheto:
    def __init__(self):
        self.savegnago_url = "https://imagens.savegnagoonline.com.br/jornal-semanal-app/Rio_Claro.pdf"

    def baixar_folheto(self, nome_arquivo="ofertas.pdf"):
        try:
            res = requests.get(self.savegnago_url, headers={'User-Agent': 'Mozilla/5.0'})
            """with open("ofertas.pdf", "wb") as f:
                f.write(res_pdf.content)
            print(f"✓ PDF baixado com sucesso! Tamanho: {len(res_pdf.content)} bytes")
            print(f"✓ Arquivo salvo como: ofertas.pdf")"""
            if res.status_code == 200:
                with open(nome_arquivo, "wb") as f:
                    f.write(res.content)
                return True
            return False
        except Exception as e:
            print(f"Erro ao baixar o PDF: {e}")
            return False
        
if __name__ == "__main__":
    downloader = folheto()
    sucesso = downloader.baixar_folheto()
    if sucesso:
        print("Download concluido, arquivo ofertas.pdf foi gerado")
    else:
        print("Falha no download")
    
