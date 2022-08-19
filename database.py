import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        data = sqlite3.connect("BaiyokeTower.db")
        return data
    except Error:
        print(Error)

def sql_add_user(email, name, last_name, password):
    strsql = f"INSERT INTO Users (email, name, last_name, password) VALUES ('{email}', '{name}', '{last_name}', '{password}');"

    data = sql_connection()
    cursor_obj = data.cursor()
    cursor_obj.execute(strsql)

    data.commit()
    data.close()

def sql_check_user():
    strsql = "SELECT email, password FROM Users;"

    data = sql_connection()
    cursor_obj = data.cursor()
    cursor_obj.execute(strsql)
    chek_user = cursor_obj.fetchall()
    data.close()

    return chek_user