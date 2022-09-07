#Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
 # Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random
def func(n):
    x = random.randint(1, 100)
    if n == 1:
        return [x]
    else:
        return func(n-1) + [x]
c = func(10)
print(c)
print(sum(c))