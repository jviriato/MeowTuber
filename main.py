from flask import Flask, url_for, render_template, request, redirect, url_for

app = Flask(__name__)
# url_for('static', filename='main.css')

@app.route('/', methods=['POST', 'GET'])
def index(bad_words = None):
    if request.method == 'POST': 
        return redirect(url_for('admin'))
    else:
        return render_template('index.html', bad_words=bad_words)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    text = request.form['text']
    return 'You entered: {}'.format(text)

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/text')
def text():
    return 'text'

if __name__ == '__main__':
    app.run(debug=True)    