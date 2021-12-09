import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com/")
soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find('div', attrs={'class' : 'service_area'})
all_a = div.findAll('a')
print(all_a[1].text)
