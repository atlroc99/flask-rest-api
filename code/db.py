import sqlite3
import os
# import os.path
from os import path
import logging


# create connection
# sqllite stores all of it's data in a file, you can name the file anything you want
# fileExists = path.exists('data.db')
# if fileExists:
#     os.remove('data.db')

# print(f"file has been deleted: {not path.exists('data.db')}")

# create connection to sqllite db
# connection = sqlite3.connect('data.db')

# create a cursor which will be used to execute sql query and statements
# cursor = connection.cursor()

# create table user with 3 fields
# insert_user = "INSERT INTO user VALUES(?,?,?)"
# user = (1, 'mohamad', 'omar123')
# select_user = "SELECT * FROM user"

# create table
# cursor.execute(create_table)

# perform insert user
# cursor.execute(insert_user, user)
# users = cursor.execute(select_user)

# print(f"tuple size: {type(users)}")
# for user in users:
#     print(user)
#     print(f"tuple length: {len(user)}")
#     print("\n")
#     for u in user:
#         print(f"{type(u)} : {u}")


def create_table():
    fileExists = path.exists('data.db')
    if fileExists:
        print("delete file...")
        os.remove('data.db')

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    create_table = "CREATE TABLE user (id int, name text, password text)"

    cursor.execute(create_table)
    connection.close()


def insert_multiple_users():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    print("inside multiple users")
    users = [
        (2, "brad", "xyz"),
        (3, "david", "abc"),
        (4, "ron", "efg"),
        (5, "okja", "hij"),
        (6, "samuel", "klm"),
    ]
    cursor.executemany("INSERT INTO user VALUES (?,?,?)", users)
    _all = cursor.execute("select * from user").fetchall()
    print(_all)
    
    connection.close()


def fetch_all_users():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    user = (1, 'Zaman', 'dfafad')
    insert_sql = "INSERT INTO user VALUES (?,?,?)"
    cursor.execute(insert_sql, user)
    _all = cursor.execute("select * from user").fetchall()
    print(f"fetch all users: {_all}")
    
    connection.close()
    return _all


create_table()
insert_multiple_users()
fetch_all_users()
# print(f"all users size: {len(all_users)}")
# print(f"fetched all users: {all_users} ")
