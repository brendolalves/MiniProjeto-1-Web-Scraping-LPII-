# **Mini Projeto - Web Scraping**

### *Este projeto consiste em um sistema de automação desenvolvido em Python para realizar o web scraping de informações diárias e enviar um relatório consolidado por e-mail. O sistema busca dados históricos, religiosos e ofertas comerciais de fontes distintas, organizando-os de forma clara e eficiente.*

## **Funcionalidades**

O sistema opera de forma automatizada para coletar os seguintes dados:

    * Wikipédia: Acessa a página principal para extrair a seção "Neste dia na história" e as curiosidades do "Sabia que...".

    * Liturgia Diária (Paulus): Coleta o Evangelho do dia diretamente do portal da Paulus.

    * Ofertas Savegnago: Realiza o download automático do folheto semanal de ofertas da unidade de Rio Claro/SP em formato PDF.

    * Relatório por E-mail: Consolida todas as informações (texto do Evangelho, fatos históricos e o anexo das ofertas) e envia para um destinatário via protocolo SMTP.

## *Estrutura do Projeto*

*O projeto foi dividido em módulos para facilitar a manutenção e seguir boas práticas de programação:* 
### Arquivo	Descrição
* app.py:	Arquivo principal que gerencia a integração dos módulos e o envio do e-mail.
* evangelho.py:	Script responsável pelo scraping do Evangelho.
* wikipedia.py:	Script focado na extração de dados da Wikipédia.
* pdf.py:	Gerencia o download do folheto de ofertas.
* Evangelho_do_dia.txt:	Arquivo temporário gerado com o conteúdo da liturgia.
* historico_wikipedia.txt:	Arquivo temporário gerado com os eventos históricos do dia.
* ofertas.pdf:	O arquivo PDF baixado com as promoções vigentes.

## *Configuração e Segurança*

Para garantir a segurança das suas credenciais e evitar a exposição de senhas no código-fonte, o projeto utiliza variáveis de ambiente.
Requisitos

    Python 3.x

    Bibliotecas necessárias (ver requirements.txt):

        requests

        beautifulsoup4

        python-dotenv

        fpdf2
        
        PyPDF2

## **Configuração do arquivo .env**

Crie um arquivo chamado .env na raiz do projeto e adicione suas informações:
Snippet de código

EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_de_aplicativo

    Nota: Se estiver usando o Gmail, lembre-se de gerar uma "Senha de Aplicativo" nas configurações da sua conta Google para que o script tenha permissão de envio.
