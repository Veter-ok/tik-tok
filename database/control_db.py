import sqlite3

# подключаемся к базе данных
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# создаём таблицу в базе данных
cur.execute("""CREATE TABLE users(
	userid INT PRIMARY KEY,
	name TEXT,
	price INT
);""")

# добавляем данные в таблицу
cur.execute("""INSERT INTO users(userid, name, price) 
VALUES('0001', 'Tom', '100000');""")

cur.execute("""INSERT INTO users(userid, name, price) 
VALUES('0002', 'Bob', '150000');""")

#читаем данные из таблицы
for row in cur.execute("SELECT * FROM users"):
	print(row)

# подтверждаем изменения и закрываем db
conn.commit()
conn.close()