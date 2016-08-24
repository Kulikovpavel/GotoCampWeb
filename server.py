from flask import *
import random
import json


app = Flask(__name__)


# вывести список значений в шаблоне templates/part1.hmtl
@app.route('/part1')
def list_view():
    l = [1, 2, 3, 4, 5, 6]
    return render_template('part1.html', l=l)

# извлечь данные из файла db.json и по id вывести информацию об объекте
@app.route('/part2/<int:id>')
def user_view(id):
    pass    

# вернуть в формате json словарь {'ans': xxx} с ответом из сложения двух GET-параметров, val1 и val2 
@app.route('/part3')
def add_numbers_view():
	pass

# обработать POST запрос и добавить к массиву из db.json новый элемент с указанным именем
# id - произвольное число
# вернуть словарь {'id': xxx} с id созданного элемента
# форма ввода по адресу /post_test
@app.route('/part4', methods=['POST'])
def add_user():
	id = random.randint(1, 100000)
	return jsonify({'id': id})

# вывести через шаблон список всех пользователей из файла db.json, 
#в виде ссылки на страничку каждого пользователя, см часть 2 задания
@app.route('/part5')
def all_users():
	pass



# не трогать, можно протестировать предыдущее задание по пути /post_test
@app.route('/post_test')
def post_test():
	return render_template('post_test.html')

# главная страничка
@app.route('/')
def index_view():
	return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()