import sqlite3
conn = sqlite3.connect('dom_2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_2 INTEGER)''')
a = [23, 'house', 'cat', 45, 'car', 66]
for i in a:
    if type(i) is str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES(?)''', (i,))
        l = len(i)
        cursor.execute('''INSERT INTO tab_2(col_2) VALUES (?)''', (l,))
    elif type(i) is int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_2) VALUES(?)''', (i,))
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES('Нечетное')''')

conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k1 = cursor.fetchall()
print(k1)
cursor.execute('''SELECT*FROM tab_2''')
k2 = cursor.fetchall()
print(k2)
if len(k2) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')

conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k1 = cursor.fetchall()
print(k1)
cursor.execute('''SELECT*FROM tab_2''')
k2 = cursor.fetchall()
print(k2)
