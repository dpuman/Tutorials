# Filter Syntax: list(filter(function, list))
from re import T


def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


def g10(num): return num > 10


l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]
test = []
for i in l:
    test.append(greater_than_5(i))

print('TEST', test)

print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))
