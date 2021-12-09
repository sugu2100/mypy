#컴파일러 vs 인터프리터
languages = ['python', 'C', 'Java', 'javaScript']

for lang in languages:
    if lang in ['python', 'javaScript']:
        print("%s need interpreter" % lang)
    elif lang in ['C', 'Java']:
        print("%s need complier" % lang)
