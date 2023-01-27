
lis = [1, 3, 5, 7, 9, ]


def sqaure(a):
    return a*a


def cube(a):
    return a*a*a


display = [sqaure, cube]

for i in lis:
    result = list(map(lambda x: x(i), display))
    print(result)
