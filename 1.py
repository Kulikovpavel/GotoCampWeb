from flask import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	return '<a href="https://ya.ru">hello, world</a>'

@app.route('/hello')
def hello_func():
	print(url_for('blog_f', user_id=13))
	return 'hello page'

@app.route('/blog/<int:user_id>')
def blog_f(user_id):
    return 'blog ' + str(user_id)


app.debug = True
app.run(host='0.0.0.0', port=80)