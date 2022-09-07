numb = 31
guess = int(input('Введите возраст Саши:'))
if guess == numb:
    print('Поздравляю! Вы заслужили леденец.')
elif guess > numb:
    print('Неужели он такой старый?')
    input('Попробуйте еще раз:')
else:
    print('Неужели он такой молодой?')
    input('Попробуйте еще раз:')