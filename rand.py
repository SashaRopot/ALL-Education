import random

str_='Hello, world'


a = random.random() #вещественное число от 0 до 1
b = random.uniform(10,100) #вещественное
c = random.randint(1,100) #целое от 1 до 100
r = random.choice(str_)

print(a,b,c,r) #Ctrl +? код в комментарий
# print(b)
# print(c)
# print(r)
print('0-1',a,'float',b,'int',c,r)