import json

from flask import Flask, request, url_for, render_template

from WriteReadFunctions import *

app = Flask(__name__)


@app.route('/view/<filename>')
def html_render(filename):
    return render_template(f'{filename}.html')


@app.route('/')
def main():
    return html_render('index')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        data_of_user = check_password(data['username'], data['passwrod'])
    except BasePostsException:
        return '-1'
    return data_of_user['id']


@app.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()
    try:
        data_of_user = create_user(data['username'], data['passwrod'], data['type'])
    except BasePostsException:

        return '-1'

    return data_of_user['id']


@app.route('/solutions')
def get_solutions():
    response = get_solutions_from_data_base()
    response = map(str, response)
    response = map(lambda x: x.replace("'", '"'), response)
    response = '/n'.join(response)
    return response


@app.route('/Quests')
def get_quests():
    response = get_quests_from_data_base()
    response = map(str, response)
    response = map(lambda x: x.replace("'", '"'), response)
    response = '/n'.join(response)
    return response


@app.route('/typeofuser', methods=['POST'])
def get_type_of_user():
    data = request.get_data()
    data_of_user = get_user_from_database(int(data))
    return str(data_of_user[4])


@app.route('/username', methods=['POST'])
def get_username():
    data = request.get_data()
    data_of_user = get_user_from_database(int(data))
    return data_of_user[1]


@app.route('/newQuest', methods=['POST'])
def new_post():
    data = request.get_json()

    username = get_user_from_database(data['id_of_user'])[1]
    content = data['content']
    create_post(username, content)
    return '1'


@app.route('/newPost', methods=['POST'])
def new_sol():
    data = request.get_json()

    username = get_user_from_database(data['id_of_user'])[1]
    content = data['content']
    create_solution(username, content)
    return '1'


if __name__ == '__main__':
    app.run()
