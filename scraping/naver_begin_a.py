from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("http://www.naver.com")
html = BeautifulSoup(url, 'html.parser')

div = html.find('div', {'class':'service_area'})
all_a = div.findAll('a')
print(all_a[1])
print(all_a[1].text)

