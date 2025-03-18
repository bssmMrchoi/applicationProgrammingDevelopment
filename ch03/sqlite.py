import sqlite3

# 데이터베이스 연결 (파일이 없으면 자동 생성됨)
# 커서(Cursor) 객체 생성
conn = sqlite3.connect("example.db")
cur = conn.cursor()

# 테이블 생성
cur.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

cur.execute("INSERT INTO person (name, age) VALUES (?, ?)", ("choi", 25))
name = "jung"
age = 30
cur.execute(f"INSERT INTO person (name, age) VALUES ('{name}', {age})")
conn.commit()  # 변경 사항 저장

cur.execute("SELECT * FROM person")
rows = cur.fetchall()
for row in rows:
    print(row)

query = "UPDATE person SET age = :age WHERE name = :name"
params = {"name": name, "age": 31}
cur.execute(query, params)
conn.commit()

cur.execute("SELECT * FROM person")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("DELETE FROM person WHERE name = ?", ("Bob",))
conn.commit()

cur.close()
conn.close()