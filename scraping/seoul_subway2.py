import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 지하철 사진 경로 출력
target_img = soup.find('img', attrs={'alt':'Seoul-metro-2009-20180916-103548.jpg'})
print(target_img)

# 소스 사진 읽어오기
target_img_src = target_img.get('src')  # 이미지 경로 가져와서 저장
print("이미지 파일 경로:", target_img_src)

target_img_response = requests.get('http:' + target_img_src) #이미지 경로 url 저장

# 바이너리 파일 모드로 파일에 쓰기
with open("./output/subway_train.jpg", 'wb') as f:
    f.write(target_img_response.content) # 이미지 - content 속성 사용
    print("이미지 파일로 저장했습니다.")

