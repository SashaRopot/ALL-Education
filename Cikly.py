# # a = input('Введите трехзначное число:')
# # d1 = int(a[0])
# # d2 = int(a[1])
# # d3 = int(a[2])
# # print('Сумма цифр данного числа равна:', d1 + d2 + d3)
# a = input('Введите трхзначное число:')
# summ = 0
# for i in a:
#     summ += int(i)
# print(summ)

# for i in range(1,10):
#     i -= 5
# print(i)

# i = 0
# while i < 10:
#     i += 1
# i -= 10
# print(i)

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)