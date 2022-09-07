# Создать кортеж с цифрами от 0 до 9 и посчитать сумму
import random
a = [random.randint(0, 9) for i in range(10)]
a = tuple(a)
print(a)
print(sum(a))