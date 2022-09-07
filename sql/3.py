import sqlite3
#Создаем базу данных
conn = sqlite3.connect('name2.db')
#Создаем обьект cursor, который позволяет нам взаимодецствовать с базой данных и добавлять записи
cursor = conn.cursor()
#Создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INEGER)''')
#Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES('hello','world', 15)''')
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
#Использование функции fetchone для получения первого результата
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchone()
print(k)
#Список всех записей отсортированных относительно третьей колонки
cursor.execute('''SELECT * FROM tab_1 ORDER BY col_3 DESC''')
conn.commit()
k = cursor.fetchall()
print(k)
#
cursor.execute('''SELECT * FROM tab_1 WHERE col_3 LIKE '3%' ''')
conn.commit()
k = cursor.fetchall()
print(k)