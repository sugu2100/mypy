
with open('c:/pyfile/food.jpg', 'wb') as f:
    data = f.read()
    img = data.decode()
    print(data)