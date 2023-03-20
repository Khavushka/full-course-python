# Неизменяемые объектов в Python
first_num = 10
second_num = first_num
print(id(first_num))
print(id(second_num))

second_num += 5
print(second_num)
print(first_num)

print(id(second_num))
print(id(first_num))

# Изменение объектов в Python
