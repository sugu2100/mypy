import pickle

with open('data.txt', 'wb') as f:
    li = ['강아지', '고양이', '닭']
    dic = {1:'강아지', 2:'고양이', 3:'닭'}
    pickle.dump(li, f)
    pickle.dump(dic, f)

with open('data.txt', 'rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)
