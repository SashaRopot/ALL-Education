#Создайте функцию, добавьте в неё локальное значение. Сделайте так, чтобы другая
# функция принимала это значение в качестве параметра

def func():
    global a
    a = 3
    return a + 6
def func_2(a):
    b = 4
    return 6*(a+b)
print(func())
print(func_2(a))