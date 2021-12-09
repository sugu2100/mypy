from urllib import request

url = "https://www.naver.com"
content = request.urlopen(url)
print(content)
print(content.read())

"""
contents = request.urlopen(url)
print(contents.read())
"""