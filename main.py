from flask import *
from firebase import firebase
import webbrowser

firebase = firebase.FirebaseApplication('https://collins-gre-8f1e6.firebaseio.com/', None)
app = Flask(__name__)

@app.route('/')
def words():
    result = firebase.get('/', '')
    if result is None:
        error = 'no record found on database'
        return render_template('index.html', error= error)
    print(result)
    return render_template('words.html', t = result)


@app.route('/modify', methods = ['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if (request.form['word'] == "" or request.form['meaning'] == "") and request.form['submit'] == 'add':
            error = 'Please input both word and message'
            return render_template('index.html', error = error)
        elif (request.form['word'] == "" and request.form['meaning'] == "") and request.form['submit'] == 'delete':
            error = 'Please enter which word to delete'
            return render_template('index.html', error = error)
        elif request.form['submit'] == 'add':
            result = firebase.get('/', '')
            flag = 1
            words = {}
            words['word'] = request.form['word']
            words['meaning'] = request.form['meaning']
            words['example'] = request.form['example']
            for j in result:
                if j['meaning'].lower() == words['meaning'].lower():
                    flag = 0
                    error = 'word already exists'
                    return render_template('index.html', error= error)
                    break
            if flag == 1:
                result.append(words)
            firebase.put('/','/', result)
            return render_template('index.html')
        elif request.form['submit'] == 'delete':
            word = request.form['word']
            meaning = request.form['meaning']
            result = firebase.get('/', '')
            for i in result:
                if i['word'].lower() == word.lower() or i['meaning'].lower() == meaning.lower():
                    result.remove(i)
            firebase.put('/','/', result)
            return render_template('index.html')
        elif request.form['submit'] == 'view':
            return redirect('/')       
    return render_template('index.html')

if __name__ == '__main__':
    # webbrowser.open('http://localhost:5000', new=2)
    app.run(debug = True)