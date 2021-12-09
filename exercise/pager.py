# 게시판 페이징
# 페이지당 보여줄 게시글 수 - 10개
# 게시글 5개 - 1page, 게시글 12개 - 2page

def getTotalPage(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1

p1 = getTotalPage(5, 10)
print(p1)
p2 = getTotalPage(13, 10)
print(p2)
p3 = getTotalPage(26, 10)
print(p3)

"""
# 실패
f1 = getTotalPage(10, 10)
print(f1)
f2 = getTotalPage(20, 10)
print(f2)
"""
