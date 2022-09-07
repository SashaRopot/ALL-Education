#Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
#Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
#После этого удалите созданную папку.
#Все операции выполнять с помощью встроенных функций библиотеки os

import os
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('Desktop')
os.mkdir('Files Python')
os.chdir('Files Python')
os.mkdir('test_1.txt')
os.mkdir('test_2.txt')
os.mkdir('test_3.txt')
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.rmdir('rename_1.txt')
os.rmdir('rename_2.txt')
os.rmdir('rename_3.txt')
os.chdir('..')
os.rmdir('Files Python')