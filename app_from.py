from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        result_info = request.form
        return render_template("result.html", result=result_info)
    else:
        print('123')


if __name__ == '__main__':
    app.run(debug=True)
