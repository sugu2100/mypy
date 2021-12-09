from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("https://www.naver.com/")
html = BeautifulSoup(url, 'html.parser')
ul = html.find('ul', {'class':'list_nav type_fix'})
#print(ul)
lis = ul.findAll('li')
print(lis)
for li in lis:
    a = li.find('a')
    print(a.text)

# 직접 a 태그로 접근
all_a = ul.findAll('a')
for a in all_a:
    print(a.text)

# '카페' 접근
print(all_a[1].text)

