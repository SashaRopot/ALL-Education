# a = {}
# print(type(a))
a = {'1': 123, 2:'hello'}
a['3'] = 5
a[7] = (2, 4, 5, 6, 3, 6)
print(a[7][2])
# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1,1),(2,'tree')])
# print(d)
# print(d_2)

# d = dict.fromkeys(['a','b'])
# d_2 = dict.fromkeys(['a','b'],100)
# print(d)
# print(d_2)

d = {a: a**2 for a in range(7)}
print(d)

# a = [1, 2, 3, 4, 5]
# b = ['hello', 'world', 'sun', 'daddy', 'mummy']
# d = dict(zip(a,b))
# print(d)