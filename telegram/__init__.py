import sqlite3
conn = sqlite3.connect("Dom_Telegram.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT,
us TEXT,
ph VARCHAR(30)''')
cursor.execute('''INSERT INTO book(us, ph) VALUES(?, ?)''', (user, phone))
conn.commit()
cursor.execute('''SELECT*FROM book''')
p = cursor.fetchall()
print(p)
