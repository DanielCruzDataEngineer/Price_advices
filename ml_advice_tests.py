import bs4
import requests
import smtplib
import time
from lxml import etree
headers = {'referer': 'https://www.google.com/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

def mercadoPrice(productUrl):

    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    dom = etree.HTML(str(soup))
    discount = soup.find('div', class_='price-tag discount-arrow arrow-left')
    elems = dom.xpath('//div[@class="a-section a-spacing-micro"]//span[@class="a-offscreen"]/text()')[0]
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

def sendEmail(price, productUrl):
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    title = soup.title.text.strip()
    dom = etree.HTML(str(soup))
    frete = dom.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]//span[@class="a-text-bold"]/text()')[0]

    conn = smtplib.SMTP('smtp.gmail.com', 587) # Se o seu email for do gmail
    conn.ehlo() 
    conn.starttls() 
    conn.login('danielcruz.alu.lmb@gmail.com', 'ttcufsrumnfwxgsi') # Email e senha
    from_ = 'danielcruz.alu.lmb@gmail.com'
    to_ = 'danielcruz.alu.lmb@gmail.com'
    subject = '{} abaixo do preço estipulado!'.format(title)
    body = '{} está a R${} no momento.\n Previsão de frete : {} Confira no link: {}\n\n-Mercado Livre Price Bot'.format(title, price,frete, productUrl)
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
mon_1 = 'https://www.amazon.com.br/Monitor-Gamer-AOC-SPEED-75Hz/dp/B08TMTQH9H/ref=d_pd_sbs_sccl_2_2/145-5883709-5729137?pd_rd_w=o5CMs&content-id=amzn1.sym.d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_p=d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_r=MSEQB8YCV8QAM4KQS287&pd_rd_wg=cNHlm&pd_rd_r=b1010606-f923-4687-9547-8d61df5819b7&pd_rd_i=B08TMTQH9H&psc=1'
mon_2 = 'https://www.amazon.com.br/Samsung-Monitor-24-F24T350FHL-Preto/dp/B098ZLDFG7/ref=d_pd_sbs_sccl_2_3/145-5883709-5729137?pd_rd_w=o5CMs&content-id=amzn1.sym.d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_p=d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_r=MSEQB8YCV8QAM4KQS287&pd_rd_wg=cNHlm&pd_rd_r=b1010606-f923-4687-9547-8d61df5819b7&pd_rd_i=B098ZLDFG7&psc=1'
mon_3 = 'https://www.amazon.com.br/Monitor-LG-Widescreen-24MP400-23-8-Preto/dp/B09HYTW34G/ref=d_pd_sbs_sccl_2_1/145-5883709-5729137?pd_rd_w=pa8yo&content-id=amzn1.sym.d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_p=d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_r=Z2RG0NW7K43FQNJXXK81&pd_rd_wg=cG6bJ&pd_rd_r=5ad680e1-c7c0-4f3f-b716-50b42e782801&pd_rd_i=B09HYTW34G&psc=1'
mon_4 = 'https://www.amazon.com.br/Monitor-LG-23-8-Widescreen-Full/dp/B07MTYSFDT/ref=d_pd_sbs_sccl_2_8/145-5883709-5729137?pd_rd_w=YpGbB&content-id=amzn1.sym.d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_p=d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_r=YKQYNNXSBBZN1BSSPVXN&pd_rd_wg=eU13Q&pd_rd_r=89ee0dc1-2a93-40a8-ad9e-e0a3cdbc97ac&pd_rd_i=B07MTYSFDT&psc=1'

# Não se esqueça de também adicionar o item aqui, junto com o preço
itens = [{'url': mon_1, 'price': 836.1, 'email': False, 'store': 'mercado'},
{'url': mon_2, 'price': 879.0, 'email': False, 'store': 'mercado'}, #899
{'url': mon_3, 'price': 818.9, 'email': False, 'store': 'mercado'},
{'url': mon_4, 'price': 799.0, 'email': False, 'store': 'mercado'}
]


if __name__=='__main__':
    checkPrice(itens) # Aqui é o tempo em que o programa irá rodar; no momento está em 1 hora (3600s)