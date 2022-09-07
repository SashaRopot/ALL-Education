def func_1():
    print('hello')
def func_2(c, d, a = 5,b = 4):  #параметры
    return a+b+c+d
    # c = a+b
    # print(c)
def func_3(*args,**kwargs):
    print(kwargs)
    print(args)
func_3(1,2,3,5,3,2,5,7,a=5,b=8,c=4)
print(func_2(8,9))
func_1()
# print(func_2(int(input()),int(input())))  #аргументы

