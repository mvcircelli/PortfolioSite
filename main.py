#Portfolio Website!

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hardware')
def hardware():
    return render_template('left-sidebar.html')

@app.route('/software')
def software():
    return render_template('right-sidebar.html')

@app.route('/contactme')
def contact():
    return render_template('no-sidebar.html')

if __name__ == '__main__':
    app.run(debug=True)