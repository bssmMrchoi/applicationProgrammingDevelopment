from sqlite3 import connect, Connection, Cursor
from typing import Optional

con: Optional[Connection] = None
cur: Optional[Cursor] = None


def get_db():
    global con, cur
    if con is None:
        print("create")
        con = connect('./mydb.db', check_same_thread=False)
        cur = con.cursor()


get_db()