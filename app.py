# 创建项目app
from flask import Flask, request, make_response
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('测试代码')
    return 'Hello World!'


@app.route('/user/<username>')
def username_page(username):
    return "User: %s" % username


@app.route('/test')
def test_url_for():
    print(url_for('hello_world'))
    print(url_for('username_page', username='MamLegion'))
    return "Test Page"


@app.route('/insert', methods=['POST'])
def post():
    info = request.json
    name = info['name']
    age = info['age']
    age_after_10_years = age + 10
    message = f'此人名叫：{name}, 10年后，此人年龄：{age_after_10_years}'
    return {'success': 'True', 'msg': message}


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
