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

    user2 = User()
    user2.surname = 'Nastya'
    user2.name = "Peace"
    user2.age = "13"
    user2.position = 'serjant'
    user2.speciality = 'research engineer'
    user2.address = 'module_2'
    user2.email = "greenpeace@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user2)

    user3 = User()
    user3.surname = 'Ivan'
    user3.name = "Ivanov"
    user3.age = "19"
    user3.position = 'cap'
    user3.speciality = 'research engineer'
    user3.address = 'module_3'
    user3.email = "ivanushki_international@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user3)

    user4 = User()
    user4.surname = 'Nyton'
    user4.name = "Zendea"
    user4.age = "24"
    user4.position = 'op op'
    user4.speciality = 'research engineer'
    user4.address = 'module_4'
    user4.email = "kyraga@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user4)

    db_sess.commit()


if __name__ == '__main__':
    main()