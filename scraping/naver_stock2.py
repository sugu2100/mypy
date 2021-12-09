from urllib import request
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + item_code
    html = request.urlopen(url)
    content = BeautifulSoup(html, 'html.parser')
    return content

def get_price(item_code):
    content = getcontent(item_code)
    # no_today = content.find('p', {'class':'no_today'})
    no_today = content.select_one("p.no_today")
    # price = no_today.find('span', {'class':'blind'})
    price = no_today.select_one("span.blind")
    return price

삼성전자 = get_price("005930")
네이버 = get_price("035420")
카카오 = get_price("035720")
print("삼성전자 주가 : {}원".format(삼성전자.text))
print("네이버 주가 : {}원".format(네이버.text))
print("카카오 주가 : {}원".format(카카오.text))
