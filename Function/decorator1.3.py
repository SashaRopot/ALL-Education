def header(func):

    def inner(*args,**qwargs):
        print('<h1>')
        func(*args,**qwargs)
        print('</h1>')

    return inner

def table(func):

    def inner(*args,**qwargs):
        print('<table>')
        func(*args,**qwargs)
        print('</table>')

    return inner

def say(name,surname,age):
    print('hello',name,surname,age)


say = table(header(say))
say('vania','ivanov',30)