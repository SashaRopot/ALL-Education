# def square(x):
#     print(x**2)
# a = square(6)
# print(a)

def square(x):
    return x**2
a = square(square(3))

def example():
    print(1)
    print(2)
    return 'hello'
    print(3)


# def even(x):
#     return x%2==0
# for i in range(1,11):
#     print(i,even(i))


def factorial(x):
    pr=1
    for i in range(2,x+1):
        pr=pr*i
    return pr

def sochet(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(sochet(5,3))