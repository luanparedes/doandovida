import sqlite3


class Dao:
    sql = ''

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

        except ZeroDivisionError:
            print(sqlite3.OperationalError)

    def fill_database(self, model):
        self.sql = 'INSERT INTO donator (email, password, name, cpf, rg, cep, street, number,' \
                                    ' complement, neighborhood,city, state, tel, cel, height, weight, blood_type) '

        self.sql = self.sql + \
            f'VALUES("{model.email}", "{model.password}", "{model.name}", "{model.cpf}", "{model.rg}", ' \
            f'"{model.adress.cep}", "{model.adress.street}",{model.adress.number}, "{model.adress.complement}", ' \
            f'"{model.adress.neighborhood}", "{model.adress.city}","{model.adress.state}", "{model.tel}", ' \
            f'"{model.cel}", {model.height}, {model.weight}, "{model.blood_type}")'

        return self.sql
