# 'ab' - сокрашение от 'a'dress 'b'ook
ab = {'Swaroop' : 'swaroop@swaroopch.com', 'Larry': 'larry@wall.org', 'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'}
print("Адресс Swaroop'a: ", ab['Swaroop'])
#Удаление пары ключ-значение
del ab['Spammer']
print('\nВ адресной книге {0} контакта\n'.format(len(ab)))
for name, adress in ab.items():
    print('Контакт {0} с адрессом {1}'.format(name,adress))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print(ab)