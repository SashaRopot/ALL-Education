#Рекурсивная и анонимная функции
def factorial(n):
    if n!=0:
        print(n)
        return n*factorial(n-1)
    else:
        return 1
print(factorial(4))
# product = lambda x,y:x+y
# print(product(2,1))