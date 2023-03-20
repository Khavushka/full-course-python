# Неизменяемые объектов в Python
first_num =  10
second_num = first_num
print(id(first_num))
print(id(second_num))

second_num += 5
print(second_num)
print(first_num)

print(id(second_num))
print(id(first_num))

# Изменение объектов в Python
my_list = [1, 2, 3]
print(id(my_list))

other_list = [1, 2, 3]
other_list.append(4)
print(other_list)
print(id(other_list))

# print(id[1, 2, 3])


info = {
    'name': 'Alla',
    'singer': True,
    'reviews': []
}
info['country'] = 'Russia'
print(info)
info_copy = info
info_copy['age'] = 100
print(info_copy)
info_copy.pop('age')
print(info_copy)
print(dir(dict))

'''
Posle kopirovaniya inzmenyaemyh objektov izmeneniya otrazhayutsya na vseh kopiyah
'''
# Как избежать изменения копий
# import library for at undgå redigering i stamdata
from copy import deepcopy

info_copy = info.copy()
info_copy['age'] = 90
# info_copy['reviews'].append('Great course!')
print(info_copy)

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('Great course!')

print(info)
print(info_deepcopy)

# Практика - Создание поверхностных и полных копий
info['new_key'] = 10
print(info)

