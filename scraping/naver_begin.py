import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.naver.com")    # 응답 객체 생성
html = BeautifulSoup(response.text, 'html.parser') # html 문서로 파싱

div = html.find('div', {'class' : 'service_area'})
first_a = div.find('a')
#print(first_a)
print(first_a.text)
