from flask import Flask, url_for, render_template, request, redirect, url_for, jsonify
import json
from pprint import pprint
import requests
bad_words = []
bd_count = 0

class Badword:
    def __init__(self, nome, id):
        self.id = id
        self.badword = nome

    def to_dict(self):
        return self.__dict__

def load_badwords():
    with open('badwords.json') as f:
        data = json.load(f)
    for d in data['badwords']:
        b = Badword(d['badword'], d['id'])
        bad_words.append(b)
    # print(json.dumps(bad_words[0].__dict__))

def save_file(d):
    with open('badwords.json', 'w') as outfile:
        outfile.write('{\n    "badwords":')
        json.dump(d, outfile, indent=4)
        outfile.write('\n}')

load_badwords()


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index(bad_words = None):
    return render_template('index.html')

@app.route('/submit_badword', methods=['POST', 'GET'])
def submit_badword():
    bid = int(bad_words[-1].id) + 1
    bid = str(bid).encode("utf-8").decode("utf-8") 
    badword = request.form['text']
    b = Badword(badword, bid)
    bad_words.append(b)
    d = []
    for b in bad_words:
        d.append(b.__dict__)
    return jsonify({'badwords': d})

@app.route('/admin')
def admin(bad_words = bad_words):
    print(bad_words)
    return render_template('admin.html', bad_words=bad_words)

@app.route('/admin', methods = ["POST"])
def addOne():
    bid = int(bad_words[-1].id) + 1
    bid = str(bid).encode("utf-8").decode("utf-8") 
    badword = request.form['text']
    b = Badword(badword, bid)
    bad_words.append(b)
    d = []
    for b in bad_words:
        d.append(b.__dict__)
    save_file(d)
    return jsonify({'badwords': d})


@app.route('/delete/<int:id>', methods=['POST'])
def remove(id):
    id = int(id)
    for i in bad_words:
        # print(i.id)
        # print(type(int(i.id)))
        # print(id)
        # print('ayee')
        if int(i.id) == id:
            # print('achou!')
            # print(i.nome)
            bad_words.remove(i)
    d = []
    for b in bad_words:
        d.append(b.__dict__)
    save_file(d)
    return jsonify({'badwords': d})



@app.route('/badwords', methods = ["GET"])
def returnAll():
    d = []
    for b in bad_words:
        d.append(b.__dict__)
    return jsonify({'badwords': d})

@app.route('/badwords/<string:id>', methods=['GET'])
def returnOne(id):
    id = int(id)
    return jsonify({'badword' : bad_words[id].__dict__})
        
if __name__ == '__main__':
    app.run(debug=True)    