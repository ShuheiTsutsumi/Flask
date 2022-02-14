from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

class UserInfo:
    def __init__(self, number, name, age, gender, major, picture_path):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.picture_path = picture_path

member_list = [
    UserInfo(0, '太郎', 21, '男', '法学部', 'css/image/taro.jpg'),
    UserInfo(1, '次郎', 20, '男', '理学部', 'css/image/jiro.jpg'),
    UserInfo(2, '良子', 22, '女', '文学部', 'css/image/ryoko.jpg'),
    UserInfo(3, '花子', 21, '女', '工学部', 'css/image/hanako.jpg') 
]

@app.route('/') #メインページ
def main():
    return render_template('main.html')

@app.route('/memberlist') #メンバー一覧ページ
def load_member_list():
    return render_template('member_list.html', member_list = member_list)

@app.route('/member/<int:member_number>') #メンバ―詳細ページ
def member_detail(member_number):
    for member in member_list:
        if member.number == member_number:
            return render_template("member_detail.html", member = member)
    return redirect(url_for('main'))

@app.route('/terms')
def terms_of_service():
    return render_template('terms.html')

@app.errorhandler(404) #ページが間違うとmain
def refirect_main_page(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
