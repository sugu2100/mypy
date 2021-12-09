import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):  #하위 디렉터리인지 검색
                search(full_filename)   # 재귀 함수
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':   # 하위 파이썬 파일인지 검색
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")

