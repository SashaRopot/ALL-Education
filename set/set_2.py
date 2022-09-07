a = {1, 3, 4, 5, 7, 3, 5, 7, 9}
b = frozenset([1, 23, 12, 7, 5, 3, 87, 45])

c = a|b
a.union(b)
print(b)
print(c)
print(a&b)
print(a.intersection(b))
for i in b:
    print(i)