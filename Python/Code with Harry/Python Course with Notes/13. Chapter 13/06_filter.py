# Filter Syntax: list(filter(function, list))
# from re import T

l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]

# True returns the value


def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


print(list(filter(greater_than_5, l)))


def g10(num): return num > 10


print(list(filter(g10, l)))


test = []
for i in l:
    test.append(greater_than_5(i))

print('TEST', test)
