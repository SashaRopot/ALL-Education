import random
import sqlite3
conn = sqlite3.connect("dom_1.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, 
title VARCHAR(50), 
author VARCHAR(30), 
price DECIMAL(8,2), 
amount INTEGER)''')
tit = input('Название книги: ')
aut = input('Автор книги: ')
pri = float(input('Цена: '))
amo = int(input('Количество: '))
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES(?, ?, ?, ?)''', (tit, aut, pri, amo))
conn.commit()
cursor.execute('''SELECT*FROM book''')
p = cursor.fetchall()
print(p)