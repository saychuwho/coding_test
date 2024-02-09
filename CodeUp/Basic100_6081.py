# Python Basic 100 - 6081

num = int(input(), 16)

for i in range(1, 16):
    print('%X' % num, '*%X' % i, '=%X' % (num*i), sep='')