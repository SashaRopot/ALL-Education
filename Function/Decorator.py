def decorator(func):

    def inner():
        print('stert decorator...')
        func()
        print('finish decorator...')

    return inner

def say():
    print('hello world')
def buy():
    print('buy world')

say = decorator(say)
say()
