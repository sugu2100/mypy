import requests
from bs4 import BeautifulSoup

# 네이버 증권 > 시장지표 > 환전 고시 환율
resp = requests.get("https://finance.naver.com/marketindex")
soup = BeautifulSoup(resp.text, "html.parser")
ul = soup.find('div', {'class':'market1'})
lis = ul.findAll('li')
print(lis)

for li in lis:
    exchange = li.find('span', {'class':'blind'})  # 환율 종류
    value = li.find('span', {'class':'value'})     # 환율 지수
    #print(exchange.string, ':', value.string)
    print(exchange.string.split(' ')[-1], ':', value.string)



