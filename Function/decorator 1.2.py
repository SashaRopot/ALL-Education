def decorator(func):

    def inner(*args,**qwargs):
        print('start decorator...')
        func(*args,**qwargs)
        print('finish decorator...')

    return inner

def say(name,surname,age):
    print('hello',name,surname,age)


say = decorator(say)
say('vania','ivanov',30)
