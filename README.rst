================
ML Prices Advice
================





O objetivo deste projeto é receber notificações por e-mail e mensagem do WhatsApp quando o preço de um produto no Mercado Livre cai abaixo de um valor estipulado.

Para isso, utilizamos as seguintes bibliotecas:

    bs4: para fazer a raspagem de dados no site do Mercado Livre
    requests: para fazer requisições HTTP
    smtplib: para enviar e-mails
    time: para adicionar um atraso entre as requisições
    lxml: para fazer o parsing do HTML
    dotenv: para carregar variáveis de ambiente
    os: para acessar variáveis de ambiente
    email.mime.multipart: para criar e-mails com várias partes
    email.mime.text: para adicionar texto às partes do e-mail
    twilio.rest: para enviar mensagens de texto e mídia pelo WhatsApp

O script pode ser executado no GitHub Actions, usando um cron job que verifica o preço do produto em intervalos regulares. Quando o preço do produto cai abaixo do valor estipulado, uma notificação é enviada por e-mail e WhatsApp.

O script é composto por duas funções principais: mercadoPrice e sendEmail, que são responsáveis por verificar o preço do produto e enviar notificações, respectivamente. A função send_msg é responsável por enviar as mensagens pelo WhatsApp.

O arquivo .env é utilizado para armazenar as variáveis de ambiente, como as credenciais do Gmail e do Twilio, bem como o número do WhatsApp de destino.

Instruções de uso

    Faça o clone deste repositório em sua máquina local

    Crie um ambiente virtual Python e ative-o

    Instale as dependências do projeto usando o comando pip install -r requirements.txt

    Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

    secrets_gmail: o e-mail do remetente (deve ser uma conta do Gmail)
    secrets: a senha da conta do Gmail
    twilio_id: a API key do Twilio
    phone_number: o número de telefone do destinatário (deve ser um número de celular com o prefixo do país e o código da área)

    No arquivo main.py, configure as seguintes variáveis:

    productUrl: o URL do produto no Mercado Livre
    preco_estipulado: o preço máximo que você está disposto a pagar pelo produto

    Rode o script usando o comando python main.py ou faça um push para o GitHub para rodar o script no GitHub Actions.

.. image:: https://i.pinimg.com/originals/bf/a9/28/bfa928ce10cac9daa4e96dad113891e1.gif
   :alt: Nome do GIF
