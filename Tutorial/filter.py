
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even(x):
    if(x % 2 != 0):
        return True


result = list(filter(even, lis))

print(result)
