from getpass import getpass

def login():
    # 아이디는 8자 이하, 비밀번호는 10자만 입력
    userid = input("Enter userID: ")
    userpw = getpass("Enter password: ")  # 비밀번호 감추기

    member = []
    with open('member.txt') as f:
        lines = f.readlines()
    for i in lines:   # 요소를 분리
        member.append([i[0:10], i[10:]])
    print(member)

    access = False  # 로그인 성공 여부
    for user, passwd in member:
        if user.strip() == userid and passwd.strip() == userpw:
            print("로그인에 성공하였습니다.")
            access = True
            break

    if access == False:
        print("아이디나 비번이 다릅니다.")
login()
