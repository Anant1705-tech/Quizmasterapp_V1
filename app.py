from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')


def login_page():
    return render_template('Login Page.html')

if __name__ == '__main__':
    app.run(debug=True)  