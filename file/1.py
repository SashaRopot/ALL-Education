# f = open('text.txt','a')
# print(f.readlines())

# for i in f:
#     print(i)


# print(*f)
# f.close()
# f.write('sunday\nsaturday')
# l = ['hello', 'red', 'blue']
# for i in l:
#     f.write(i+'\n')

with open('text_1.txt', 'r') as f:
#     f.write('Hey')
    print(f.readlines())