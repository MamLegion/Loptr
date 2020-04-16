from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_cookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
    else:
        user = 'Not a cookie'
    response = make_response(render_template('readcookie.html'))
    response.set_cookie('userId', user)

    return response


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userId')
    return 'Welcome %s !' % name


if __name__ == '__main__':
    app.run(debug=True)
