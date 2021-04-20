from flask import Flask, render_template
from users import users
from goods import goods
app = Flask(__name__)
app.register_blueprint(users)
app.register_blueprint(goods)


@app.route('/')
def index():
    return 'welcome to BluePrint'


# 自定义状态码页面 404
@app.errorhandler(404)
def errorpage(e):
    return '此页面去度假了'


user = {
    'name': 'Kobe',
    'bio': 'A man who loves basketball.'
}
movies = [
    {'name': '蜘蛛侠', 'years': '1999'},
    {'name': '蜘蛛侠1', 'years': '2000'},
    {'name': '钢铁侠1', 'years': '2001'},
    {'name': '钢铁侠2', 'years': '2002'},
    {'name': '复仇者联盟', 'years': '2005'}
]

# jinjia2前端模版
@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)



if __name__ == '__main__':
    app.run(debug=True)
