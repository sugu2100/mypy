# 이미지 파일 읽기
with open('activity.jpg', 'rb') as f1:
    data = f1.read()

# 이미지 파일 쓰기
with open('./output/activity2.jpg', 'wb') as f2:
    f2.write(data)
