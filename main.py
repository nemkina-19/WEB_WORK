from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()
    user = User()
    user.surname = 'Scott'
    user.name = "Ridley"
    user.age = "21"
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)

    user = User()
    user.surname = 'Nastya'
    user.name = "Peace"
    user.age = "13"
    user.position = 'serjant'
    user.speciality = 'research engineer'
    user.address = 'module_2'
    user.email = "greenpeace@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)

    user = User()
    user.surname = 'Ivan'
    user.name = "Ivanov"
    user.age = "19"
    user.position = 'cap'
    user.speciality = 'research engineer'
    user.address = 'module_3'
    user.email = "ivanushki_international@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)

    user = User()
    user.surname = 'Nyton'
    user.name = "Zendea"
    user.age = "24"
    user.position = 'op op'
    user.speciality = 'research engineer'
    user.address = 'module_4'
    user.email = "kyraga@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)

    db_sess.commit()


if __name__ == '__main__':
    main()