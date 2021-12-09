from bs4 import BeautifulSoup
html_str = '''
<html>
    <body>
        <ul class = 'item'>
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇</li>
        <ul>
        <ul class = 'comlang'>
            <li>Python</li>
            <li>C/C#</li>
            <li>Java</li>
        <ul>
    </body>
</html>
'''
soup = BeautifulSoup(html_str, "html.parser")
first_ul = soup.find('ul', attrs={'class':'item'})  #dict = {} 로 찾기
all_li = first_ul.findAll('li')  # 모든 li요소를 리스트로 반환
print(all_li)
print(all_li[1])
print(all_li[1].text)

for li in all_li:
    print(li.text)

