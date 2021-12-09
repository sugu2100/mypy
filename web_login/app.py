from flask import Flask, render_template, request, session, redirect, url_for

application = Flask(__name__)
application.secret_key = "rlarldyd"
userID = "hello"
userPW = "world"
@application.route('/')
def home():
    if 'userID' in session:   # 세션 이름 발행
        return render_template('home.html', username=session.get("userID"), login=True)
    else:
        return render_template('home.html', login=False)

@application.route('/login', methods=['GET'])
def login():
    global userID, userPW
    uid = request.args.get("uid")
    pwd = request.args.get("pwd")

    if userID == uid and userPW == pwd:
        #print(uid, pwd)
        session["userID"] = uid    # userID은 세션 이름
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

# @application.route('/logout')
# def logout():
#     pass

application.run()