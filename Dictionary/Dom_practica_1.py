#Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla и списками
# из 3х моделей в качестве значений. Выведите первое и последнее значения каждого из ключей.
auto = {'BMW': ['730d', '525i', 'X5', 'M5'],
        'Tesla': ['Model S', 'Model X', 'Model 3', 'CyderTruck']}
for key,value in auto.items():
    print(key, value[0], value[-1])