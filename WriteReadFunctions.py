import datetime
import sqlite3
from MainClasses import *
import os


def check_password(username: str, password: str):
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'select * from users where username = "{username}"'
    response = cur.execute(req).fetchall()
    response = response[0]
    response = list(map(str, response))
    cur.close()
    con.cursor().close()
    con.close()
    if len(response) == 0:
        raise NotFoundUsername('Такого пользователя нет')

    if response[2] == password:
        data = {'id': response[0], 'username': username, 'password': response[2], 'date': response[3]}
        return data
    raise MismatchPassword('Пароль не совпадает')


def write_error(message: str):
    if 'logs_error' not in os.listdir():
        os.mkdir('logs_error')
    now = datetime.datetime.now()
    path = f"logs_error\\{now.strftime('%c').replace(':', '.').replace(' ', '_')}.txt"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(message)


def get_user_from_database(id_: int):
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'select * from users where id="{id_}"'
    data = cur.execute(req).fetchall()
    if len(data) == 0:
        raise NoUser('такого пользователя нет')
    data = data[0]
    cur.close()
    con.close()
    return data


def get_quests_from_data_base():
    con = sqlite3.connect('quests.sqlite')
    cur = con.cursor()
    req = f'select * from posts'
    data = cur.execute(req).fetchall()
    result = []
    for el in data:
        result.append({'id': str(el[0]), 'content': el[1], 'date': el[2], 'username': el[3]})
    cur.close()
    con.close()
    return result


def get_solutions_from_data_base():
    con = sqlite3.connect('solutions.sqlite')
    cur = con.cursor()
    req = f'select * from solutions'
    data = cur.execute(req).fetchall()
    result = []
    for el in data:
        result.append({'id': str(el[0]), 'content': el[1], 'date': el[2], 'username': el[3]})
    cur.close()
    con.close()
    return result


def create_post(username: int, content: str):
    con = sqlite3.connect('quests.sqlite')
    cur = con.cursor()
    date = datetime.date.today()
    req = f'insert into posts(username, date, content) values("{username}", "{date}", "{content}")'
    cur.execute(req)
    con.commit()
    cur.close()
    con.close()



def create_solution(username: int, content: str):
    con = sqlite3.connect('solutions.sqlite')
    cur = con.cursor()
    date = datetime.date.today()
    req = f'insert into solutions(username, date, content) values("{username}", "{date}", "{content}")'
    cur.execute(req)
    con.commit()
    cur.close()
    con.close()


def create_user(username: str, password: str, type_: str):
    date = datetime.date.today()
    con = sqlite3.connect('users.sqlite', timeout=1)
    cur = con.cursor()
    req = f'insert into users(username, password, date, type) values("{username}", "{password}", "{date}", "{type_}")'
    try:
        cur.execute(req)
        con.commit()
    except sqlite3.IntegrityError:
        cur.close()
        con.close()
        raise NicknameIsBusy('Такое имя пользователя уже используется')

    req = f'select * from users where username = "{username}"'
    response = cur.execute(req).fetchall()
    response = response[0]
    response = list(map(str, response))
    cur.close()
    con.close()
    return {'id': response[0], 'username': username, 'password': response[2], 'date': response[3]}
