from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/learn more')
def learn_more():
    return render_template('learn more.html')


@app.route('/learn more1')
def learn_more1():
    return render_template('learn more1.html')


@app.route('/learn more2')
def learn_more2():
    return render_template('learn more2.html')


@app.route('/pay')
def pay():
    return render_template('pay.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/enter')
def enter():
    return render_template('enter.html')


if __name__ == '__main__':
    app.run(debug=True)


