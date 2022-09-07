def counter(func):
    def wrapper(*args,**kwargs):
        wrapper.count +=1
        return func(*args,**kwargs)
    wrapper.count = 0
    return wrapper
@counter
def f():
    print('Hello')

f()
f()
f()
print(f.count)