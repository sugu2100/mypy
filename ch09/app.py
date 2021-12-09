from flask import Flask
app = Flask(__name__)  # app - Flask 객체 생성

@app.route('/')
def index():
    return "Hello~ flask"

@app.route('/register') # '/list'는 루트 아래 경로
def register():
    return "<h2><i>회원가입</i> 페이지입니다.</h2>"

@app.route('/login') # '/list'는 루트 아래 경로
def login():
    return "<h2><i>로그인</i> 페이지입니다.</h2>"

@app.route('/board')
def board():
    return "<h2><i>게시판</i> 페이지입니다.</h2>"

if __name__=="__main__":
    app.run()

