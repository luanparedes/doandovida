import sqlite3


class Dao:

    def verify_user(self, email, password):
        try:
            conn = sqlite3.connect('doandovida.db')
            cursor = conn.cursor()
            sql = f'SELECT email, password FROM donator WHERE email = "{email}" AND password = "{password}"'
            cursor.execute(sql)
        except Exception:
            return False

        if cursor.fetchone():
            return True

    def add_user(self, user):

        atributes = []
        commands = []
        sql = ''

        try:
            conn = sqlite3.connect('doandovida.db')
            cursor = conn.cursor()

            for enumerate, atr in atributes:
                commands.append(f'INSERT INTO donator ({atr}) VALUES ({user[enumerate]})')

            for enumerate, i in commands:
                sql = sql + commands[enumerate] + ','

            cursor.execute(sql)
        except sqlite3.OperationalError:
            pass