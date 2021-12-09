
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]  # 확장자 추출
        if ext == '.py':  # 하위 파이썬 파일인지 검색
            print(full_filename)

search("c:/")
