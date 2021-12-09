import requests
from bs4 import BeautifulSoup

# 네이버 증권 > 시장지표 > 환전 고시 환율
response = requests.get("https://finance.naver.com/marketindex")
#html = html.read().decode('euc-kr','replace').encode('utf-8', 'replace')
soup = BeautifulSoup(response.text, "html.parser")
lis = soup.select("div.market1 ul li")
#print(lis)

for li in lis:
    exchange = li.select_one("span.blind")  #환율 종류
    #print(exchange)
    value = li.select_one("span.value")     #환율 지수
    #print(exchange.string, value.string)
    print(exchange.string.split(' ')[-1], ':', value.string)



