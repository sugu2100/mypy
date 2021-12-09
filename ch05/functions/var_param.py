# 가변 매개변수 - 변수앞에 '*' 붙임
def merge_string(*text_list):
    result = ""
    for s in text_list:
        result += s
    return result

s1 = merge_string('강아지', '고양이', '닭')
print(s1)
