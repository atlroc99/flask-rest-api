import sqlite3
from db import create_table


class User:
    def __init__(self, _id, username, password):
        self._d = _id
        self.username = username
        self.password = password

    @classmethod
    def fetch_users(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM user").fetchall()
        return rows

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        result_set = connection.cursor().execute(
            "select * from user where username=?", (username, ))
        row = result_set.fetchone()
        user = None
        if row:
            # user = User(row[0], row[1], row[2])
            user = User(*row)
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        row = cursor.execute("SELECT * FROM user where id=?", (id,)).fetchone()
        if row:
            user = User(*row)

        cursor.close()
        connection.close()

        return row

    @classmethod
    def add_user(cls, user):
        print(f"Inserting user {user}")
        create_table()
        insert_query = "insert into user values(?,?,?)"
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute(insert_query, user)
        row = cursor.execute("select * from user").fetchone()
        print(row)
        return row

    @classmethod
    def add_users(cls, users:list):
        insert_query = "insert into user values(?,?,?)"
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.executemany(insert_query, users)
