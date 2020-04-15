from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('hello.html')


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


@app.route('/score/<int:num>')
def search_score(num):
    print(num)
    return render_template('hello.html', marks=num)


@app.route('/result')
def result():
    dic = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dic)


if __name__ == '__main__':
    app.run(debug=True)
