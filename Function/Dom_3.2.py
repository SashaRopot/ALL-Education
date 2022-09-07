#Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
 # Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random
b = []
for i in range(10):
    a = random.randint(1, 100)
    b.append(a)
print(b)
def func(x):
    if x == []:
        return 0
    else:
        return x[0]+func(x[1:])
print(func(b))