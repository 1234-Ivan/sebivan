from flask import Flask, render_template
import os
from db import main

app = Flask(__name__, static_folder='static', template_folder='templates')


# Максимальный размер файла (например, 16 MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# Главная страница
@app.route('/')
def index():
    return render_template('login_page.html')


# Маршрут для загрузки файла
@app.route('/log', methods=['POST', 'GET'])
def upload_file(username, password):
    user = main.Sql(username, password)
    print(username, password)
    print(user)
    return render_template('home_page.html', username=username, password=password)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)