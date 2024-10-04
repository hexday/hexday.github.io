from flask import Flask, redirect, request, render_template, url_for


app = Flask(__name__)

app.secret_key = '48f4ec2f80d984f351fc43947d55360bb1744cbb42820d2c25eeb7e5dd3a8a7c7104aa9eb3504338540bfcb7ac95a4829c1a'


@app.route('/')
def main():
    return render_template('index.html')

@app.errorhandler(400)
def notfound():
    return render_template('400.html')


@app.errorhandler(401)
def servererror():
    return render_template('401.html')


@app.errorhandler(403)
def servererror():
    return render_template('403.html')


@app.errorhandler(404)
def servererror():
    return render_template('404.html')


@app.errorhandler(405)
def servererror():
    return render_template('405.html')

@app.errorhandler(408)
def servererror():
    return render_template('408.html')

@app.errorhandler(500)
def servererror():
    return render_template('500.html')

@app.errorhandler(502)
def servererror():
    return render_template('502.html')


@app.errorhandler(503)
def servererror():
    return render_template('503.html')


@app.errorhandler(504)
def servererror():
    return render_template('504.html')
if __name__ == '__main__':
    app.run(debug=True)