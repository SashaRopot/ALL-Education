#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.
def is_prime(a):
    if a==2 or a==3: return True
    if a%2==0 or a<2: return False
    for i in range(3, int(a**0.5)+1, 2):
        if a%i==0:
            return False
    return True
print(is_prime(1))
