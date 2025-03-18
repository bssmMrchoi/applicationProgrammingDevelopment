import sqlite3
from sqlite3 import Connection, connect
from typing import Optional


class DBConnect:
    # static 변수임
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("create")
            cls._instance = super().__new__(cls)
            cls._instance.con = sqlite3.connect('./mydb.db', check_same_thread=False)
        return cls._instance

    def get_connection(self):
        return self.con


db = DBConnect()
con = db.get_connection()
cur = con.cursor()