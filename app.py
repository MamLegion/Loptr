# 创建项目app
from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
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


@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'Blog Number % d' % post_id


@app.route('/rev/<float:rev_no>')
def revision(rev_no):
    return "Revision Number %f" % rev_no


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<username>')
def hello_username(username):
    if username == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=username))


@app.route('/success/<username>')
def success(username):
    return 'Welcome %s' % username


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        print('POST:%s' % user)
        return redirect(url_for('success', username=user))
    else:
        user = request.args.get('username')
        print('GET:%s' % user)
        return redirect(url_for('success', username=user))


if __name__ == '__main__':
    app.run()
