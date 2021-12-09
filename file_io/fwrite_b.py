
with open('data.bin', 'wb') as f:
    text = "비가 내려요"
    f.write(text.encode())

with open('data.bin', 'rb') as f:
    data = f.read()
    text = data.decode()
    print(text)

