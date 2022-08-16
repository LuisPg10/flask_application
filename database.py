import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        data = sqlite3.connect("BaiyokeTower.db")
        return data
    except Error:
        print(Error)

def sql_add_user(email, name, last_name, password):
    strsql = ("INSERT INTO USERS ("+
    "email, name, last name, password) VALUES (?,?,?,?)", 
    (email, name, last_name, password))

    data = sql_connection()
    cursor_obj = data.cursor()
    cursor_obj.execute(f"{strsql}")

    data.commit()
    data.close()