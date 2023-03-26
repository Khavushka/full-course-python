# function

def sum(a, b):
    a += 1
    c = a + b
    # print(c)
    return c

res = sum(23,67)
print(res)
# print(type(sum))

# the shortest function

def my_fn():
    pass # used to block error, when it's empty

print(my_fn()) # None

# Передача неизменяемых объектов в функцию
