from bs4 import BeautifulSoup

html_str = '''
<html>
    <body>
        <ul class = 'item'>
            <li>인공지능</li>
            <li>Big Data</li>
            <li>로봇</li>
        </ul>
        <ul class = 'comlang'>
            <li>Python</li>
            <li>C/C#</li>
            <li>Java</li>
        </ul>
    </body>
</html>
'''

soup = BeautifulSoup(html_str, "html.parser")
#print(html)
first_ul = soup.find('ul')  #처음 나오는 ul태그를 찾음
print(first_ul)
print(first_ul.text)

