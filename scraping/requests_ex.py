import requests

url = "https://www.python.org"
response = requests.get(url)  # url 객체 저장
print(response)
html = response.text  # html 코드 저장
print(html)

url2 = "https://www.python.org/3"
response = requests.get(url2)
print(response)

