# Python Basic 100 - 6084

h, b, c, s = map(int, input().split())

data = (h*b*c*s)/8/1024/1024

print("{:.1f} MB".format(data))