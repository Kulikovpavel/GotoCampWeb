from flask import *
import random
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Hello World!00000</h1>
    <a href="/hello">hello link</a>'''

@app.route('/user/<int:user_id>')
def show_post(user_id):
    return 'User %s <a href="%s">Назад</a>' % (user_id, url_for('fun_hello', name="John"))


@app.route('/hello/')
@app.route('/hello/<name>')
def fun_hello(name=None):
    users = []
    with open('db.json') as f:
        users = json.load(f)

    return render_template('hello.html', name=name, users=users)

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstname']
    lastname = request.form['lastname']

    session['username'] = firstname

    with open('db.json') as f:
        users = json.load(f)
        users.append({'id': random.randrange(1,100), 'username': firstname + " " + lastname})
    
    with open('db.json', 'w') as f:
        json.dump(users, f)

    return redirect(url_for('fun_hello'))

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.debug = True
    app.run(host='0.0.0.0')

