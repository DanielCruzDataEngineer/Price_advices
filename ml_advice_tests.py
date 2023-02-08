import bs4
import requests
import smtplib
import time
from lxml import etree
from dotenv import load_dotenv,find_dotenv
import os

def mercadoPrice(productUrl):

    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    dom = etree.HTML(str(soup))
    discount = soup.find('div', class_='price-tag discount-arrow arrow-left')
    elems = dom.xpath('//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]/text()')[0]
    pricen_str = elems.strip()
    pricen_str = pricen_str.replace('.', '') # se for mais que 1.000,00
    pricen_str = pricen_str.replace(',', '.')
    pricen_str = pricen_str.replace('\n', '')
    pricen_str = pricen_str.replace('R$', '')
    

    price = float(pricen_str)
    print(price)
    if discount != None:
        discount = discount.text.strip()
        discount = float(discount[:2])/100
        price = price * (1-discount)
    return price
# /html/body/main/div[2]/div[3]/div[1]/div[2]/div/div[1]/form/div[1]/div/p/span
def sendEmail(price, productUrl):
    load_dotenv(find_dotenv())
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    title = soup.title.text.strip()
    dom = etree.HTML(str(soup))
    gamil_token = os.getenv("secrets")

    conn = smtplib.SMTP('smtp.gmail.com', 587) # Se o seu email for do gmail
    conn.ehlo() 
    conn.starttls() 
    conn.login('danielcruz.alu.lmb@gmail.com', gamil_token) # Email e senha
    from_ = 'danielcruz.alu.lmb@gmail.com'
    to_ = 'danielcruz.alu.lmb@gmail.com'
    subject = '{} abaixo do preço estipulado!'.format(title)
    imagem = dom.xpath('//img[@class="ui-pdp-image ui-pdp-gallery__figure__image"]/@src')
    body = '{} está a R${} no momento.\n Confira no link: {}\nImagem do produto no link :{} \n\n-Mercado Livre Price Bot'.format(title, price, productUrl,imagem)
    msg = 'Subject: {}\n\n{}'.format(subject, body)
    conn.sendmail(to_, from_, msg.encode('utf-8'))
    print('Email has been sent!')
    conn.quit()

def checkPrice(itens):
    for item in itens:
        if item['email'] != True:
            price = mercadoPrice(item['url'])
            if price < item['price']:
                sendEmail(price, item['url'])
                item['email'] = True

# Itens Mercado Livre:
# Aqui você pode adicionar quantas URL's quiser, aqui somente alguns exemplos
mon_1 = 'https://produto.mercadolivre.com.br/MLB-3087768923-monitor-led-22-hq-widescreen-vesa-ajuste-de-inclinaco-_JM#position=33&search_layout=grid&type=item&tracking_id=788e07de-37da-428e-a72d-ac4f0a096115'
mon_2 = 'https://produto.mercadolivre.com.br/MLB-1957277796-monitor-com-bordas-ultrafinas-215-221v8-hdmi-philips-_JM#position=31&search_layout=grid&type=item&tracking_id=199fcff5-ed27-484b-90ec-04879210a753'
mon_3 = 'https://www.mercadolivre.com.br/monitor-aoc-b1-series-24b1xhm-led-238-preto-90v240v/p/MLB18459540?pdp_filters=seller_id%3A480263032#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=d8fca78d-590a-4345-ad83-4a9e5dc97c95'
mon_4 = 'https://www.mercadolivre.com.br/monitor-gamer-lg-24mp400-lcd-238-preto-100v240v/p/MLB18910464#reco_item_pos=2&reco_backend=univb-pdp&reco_backend_type=low_level&reco_client=pdp-v2p&reco_id=624cddcf-a1a8-4b66-83ef-511f44fd3a1c'

# Não se esqueça de também adicionar o item aqui, junto com o preço
itens = [{'url': mon_1, 'price': 599.0, 'email': False, 'store': 'mercado'},
{'url': mon_2, 'price': 699.0, 'email': False, 'store': 'mercado'}, #689
{'url': mon_3, 'price': 759.0, 'email': False, 'store': 'mercado'},
{'url': mon_4, 'price': 829.0, 'email': False, 'store': 'mercado'}
]


if __name__=='__main__':
    checkPrice(itens) # Aqui é o tempo em que o programa irá rodar; no momento está em 1 hora (3600s)