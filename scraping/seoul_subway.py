import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# title 태그 요소 출력
print(soup.head)
print("title 태그 요소:", soup.title)
print("title 태그 이름:", soup.title.name)
print("title 태그 문자열:", soup.title.string)

#print(html.body)
# 지하철 사진 경로 출력
target_img = soup.find('img', attrs={'alt':'Seoul-metro-2009-20180916-103548.jpg'})
print(target_img)

