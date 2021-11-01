from model.donator import Donator
from model.bloodcenter import BloodCenter
import sqlite3

actual_login = ''


class Dao:
    donator_model = Donator()
    center_model = BloodCenter()

    sql = ''
    centers = []

    def __init__(self):
        global actual_login

        actual_login = self.initial_login()

    def verify_user(self, email, password):
        try:
            conn = sqlite3.connect('doandovida.db')
            cursor = conn.cursor()
            self.sql = f'SELECT email, password FROM donator WHERE email = "{email}" AND password = "{password}"'
            cursor.execute(self.sql)
        except Exception:
            return False

        if cursor.fetchone():
            return True

    def add_user(self, user):
        try:
            conn = sqlite3.connect('doandovida.db')
            cursor = conn.cursor()

            self.sql = self.fill_database(user)
            cursor.execute(self.sql)
            conn.commit()
            conn.close()

        except:
            pass

    def get_all_bloodcenters(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = 'SELECT * FROM blood_center'

        cursor.execute(self.sql)
        daolist = cursor.fetchall()

        for i, center in enumerate(daolist):
            self.centers.append(BloodCenter())

            self.centers[i].email = center[1]
            self.centers[i].password = center[2]
            self.centers[i].company = center[3]
            self.centers[i].cnpj = center[4]
            self.centers[i].adress.cep = center[5]
            self.centers[i].adress.street = center[6]
            self.centers[i].adress.number = center[7]
            self.centers[i].adress.complement = center[8]
            self.centers[i].adress.neighborhood = center[9]
            self.centers[i].adress.city = center[10]
            self.centers[i].adress.state = center[11]
            self.centers[i].tel = center[12]
            self.centers[i].tel2 = center[13]
            self.centers[i].next_date = center[14]

        return self.centers

    def verify_email(self, email):
        try:
            conn = sqlite3.connect('doandovida.db')
            cursor = conn.cursor()
            self.sql = f'SELECT email, password FROM donator WHERE email = "{email}"'
            cursor.execute(self.sql)
        except Exception:
            return False

        if cursor.fetchone():
            return True

    def save_last_login(self, login, password):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()
        global actual_login
        actual_login = login

        try:
            self.sql = f'UPDATE last_user SET lastuser = "{login}", password = "{password}" WHERE id = 1'
            cursor.execute(self.sql)
        except sqlite3.IntegrityError:
            self.sql = f'INSERT INTO last_user(id, lastuser, password) VALUES(1, "{login}", "{password}")'
            cursor.execute(self.sql)

        conn.commit()
        conn.close()

        return self.sql

    def recover_last_login(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        user = []

        try:
            self.sql = "SELECT lastuser FROM last_user WHERE id = 1"
            cursor.execute(self.sql)
            user.append(cursor.fetchone()[0])

            self.sql = "SELECT password FROM last_user WHERE id = 1"
            cursor.execute(self.sql)
            user.append(cursor.fetchone()[0])
        except TypeError:
            pass

        conn.close()

        return user

    def get_address(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = 'SELECT street, number, city, state FROM donator WHERE id = ' \
                   f'(SELECT id FROM donator WHERE email = "{actual_login}")'
        cursor.execute(self.sql)

        lista = cursor.fetchone()

        address = f'{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, '

        return address

    def get_blood_centers_address(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = 'SELECT street, number, city, state FROM blood_center'

        cursor.execute(self.sql)

        addresses_list = cursor.fetchall()

        return addresses_list

    #privates
    def fill_database(self, model):
        self.sql = 'INSERT INTO donator (email, password, name, cpf, rg, cep, street, number,' \
                                    ' complement, neighborhood,city, state, tel, cel, height, weight, blood_type) '

        self.sql = self.sql + \
            f'VALUES("{model.email}", "{model.password}", "{model.name}", "{model.cpf}", "{model.rg}", ' \
            f'"{model.adress.cep}", "{model.adress.street}",{model.adress.number}, "{model.adress.complement}", ' \
            f'"{model.adress.neighborhood}", "{model.adress.city}","{model.adress.state}", "{model.tel}", ' \
            f'"{model.cel}", {model.height}, {model.weight}, "{model.blood_type}")'

        return self.sql

    def initial_login(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        try:
            self.sql = 'SELECT lastuser FROM last_user WHERE id = 1'
        except:
            self.sql = 'SELECT login FROM donator WHERE id = 1'

        cursor.execute(self.sql)

        return cursor.fetchone()[0]

    def get_saved_config(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = 'SELECT * FROM config'

        cursor.execute(self.sql)

        return cursor.fetchone()

    def save_system_color(self, system_color):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = f'UPDATE config SET system_color = "{system_color}"'

        return cursor.execute(self.sql)

    def save_theme_color(self, theme):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = f'UPDATE config SET theme_color = "{theme}"'

        return cursor.execute(self.sql)

    def take_all_questions(self):
        conn = sqlite3.connect('doandovida.db')
        cursor = conn.cursor()

        self.sql = 'SELECT * FROM quiz WHERE answered = 0'

        cursor.execute(self.sql)

        return cursor.fetchall()
