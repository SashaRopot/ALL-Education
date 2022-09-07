# Есть список. Нужно отсортировать и удалить повторяющиеся элементы
a = [1, 5, 8, 8, 3, 32, 2, 86, 21, 2, 54]
d = list()
a.sort()
for i in a:
    if a.count(i) == 1:
        d.append(i)
    else:
        continue
print(d)









# b = [3]
# a.append(5)
# a.insert(2,4)
# a[1] = 3
# c = a+b
# b.extend(a)
# print(a.count(3))
# d=a.copy()
# d.append(5)
# a.append(3)
# print(d)
# print(a)
#
#
# f = [1, 4, 3, 6, 4, 9, 7]
# f.reverse()
# f.sort(reverse=True)
# print(f)