from typing import Optional

import pymysql
from pymysql.connections import Connection
from pymysql.cursors import Cursor

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='q1w2e3',
        database='study',
        port=3306
    )

con = get_connection()
cur = con.cursor()