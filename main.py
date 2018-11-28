from flask import Flask, url_for, render_template, request, redirect, url_for

bad_words = []
bd_count = 0
class Badword:
    def __init__(self, nome, id):
        self.id = id
        self.nome = nome

def load_badwords():
    global bd_count
    with open("badwords.txt", "r") as bd:
        for line in bd:
            line.replace('\n', '')
            print(line)
            bd_count += 1
            b = Badword(line, bd_count)
            bad_words.append(b)
            print(b)

load_badwords()


app = Flask(__name__)

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
def admin(bad_words = bad_words):
    print(bad_words)
    return render_template('admin.html', bad_words=bad_words)

@app.route('/text')
def text():
    return 'text'

if __name__ == '__main__':
    app.run(debug=True)    