f = open("word.txt", 'w')
word = ['sky', 'earth', 'moon', 'flower', 'tree',
         'strawberry', 'grape', 'garlic','onion', 'potato']
for i in word:
    f.write(i + ' ')
f.close()

f = open("word.txt", 'r')
data = f.read()
print(data)
f.close()
