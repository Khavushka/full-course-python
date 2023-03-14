# Несуществующие ключи и метод get
# my_moto = {
#     'brand' : 'Ducati',
#     'price' : 25000,
#     'engine' : 1.2,
# }

# print(my_moto["engine"])
# print(my_moto.get('engine', 0))

'''
Кортежи - tuple (uporyadochenya posledovatelnost elementov, ih menyat nelzya)
- v kortezhe mogut byt obekty raznyh tipov
- kruglyh skobkah
'''
# my_fruits = ('apple', 'orange', 'lime')
# print(len(my_fruits))
# print(type(my_fruits))
# print(my_fruits[-3])

# users = (
#     {
#         'user_id': 134,
#         'user_name': 'Alice'
#     },
#     {
#         'user_id': 135,
#         'user_name': 'Bob'
#     }
#     )
# print(users[1]['user_id'])
# users[1]['user_id'] = 100
# print(users[1]['user_id'])
# print(users[1])

# my_fruti = 'apple'
# other_fruti = 'orange'
# new_fruti = 'lime'
# all_fruti = (my_fruti, other_fruti, new_fruti)

# print(all_fruti)

# internal_ids = (123, 456)
# external_ids = (456, 545)
# all_ids = internal_ids + external_ids
# print(all_ids)

# Methods tuple( only two methods: count, index)
# posts_ids = (123, 456)

# posts_ids_list = list(posts_ids)
# posts_ids_list.append(345)
# # posts_ids_list.remove(123)

# print(posts_ids_list)

# posts_ids_tuple = tuple(posts_ids_list)

# print(posts_ids_tuple)

# Praktika tuple
# my_nums = (10, 5, 28, 6, 5, 6)
# my_list = list(my_nums)
# my_list.append(7)
# print(my_list)
# my_nums = tuple(my_list)
# print(my_nums)

'''
Наборы - set (neuporyadochnaya posledovatelnost elementov)
- soderzhit tolko unikalnye elementy
- esli element est, to ne dobavitsya
- izmenyat mozhno
- v naborah obychno sohranyajut odnotipnye obejkty
- ne ispolzovat [], chtoby uznat index
- indexov netu u elementov
- nelzya dobavlyat izmenyaemye objekty: list, dict, set
- nelzya udalyat s 'del'
'''
my_set = {'apple', 'android', 'iphone'}
print(type(my_set))
my_set.add('orange')

my_set2 = { 10, 45, 67}
my_set4 = { 10, 45, 67, 106, 455, 667}
# my_set2 = [10, 25, 10, 45, 67]
# print(dir(my_set2))
print(my_set2)
# UNION-method
all_sets =my_set2.union(my_set4)
print(all_sets)
# INTERSECTION-method
common_s =my_set2.intersection(my_set4)
# common_s =my_set2&(my_set4) # & - kan bruges som intersection
print(common_s)
# ISSUBSET - method
is_sub = my_set2.issubset(my_set4)
print(is_sub)
print("-------------------")
# Практика - Методы наборов
my_set5 = {'abc', 'a', 'c'}
other_set = {'a','f','c',}
print(my_set5.intersection('ab')) # dlya poiska odinakovyh 
print(my_set5.union(other_set)) # dlya obedineniya elementov
print(my_set5.issubset(other_set)) # dlya sravneniya dvuh elementov
print(my_set5 == other_set, my_set5 is other_set)
print(my_set5.difference(other_set))
print(my_set5 | other_set) # union
print(my_set5 & other_set) # intersection
print(my_set5.discard('a'))
print(my_set5)
my_set5.add('h')
other_set.add('y')
print(my_set5, '\n', other_set)
print(my_set5 & other_set) # sravnivaet obshij element
print("-----------------------------")
copied_set = my_set.copy()
print(copied_set)
print(copied_set & my_set)

# Практика - Симметричная разница в наборах
my_set.add('r')
copied_set.add('b')
# print(my_set.symmetric_difference(copied_set))
print((my_set | copied_set) - (my_set & copied_set) )

''' 
Диапазоны - range(uporyadochnaya neizmenyaemaya posledovatlnost elementov)
- Diapazony obychno ispolzuyjtsya v ciklah
- Kazhdyj diapazon - eto eksemplyar klassa range
'''
my_range = range(10, 20, 3) # 1. nachalo, 2. konec, 3. shag
print(list(my_range))
print(my_range[3]) # index poluchenie
# Практика - Диапазоны




# Min lommeregner
# print("Hej, her er min egen lommeregner. Enjoy")
# a = int(input("Enter a number: "))
# b = input("Choose a option: \nA. plus \nB. minus \nC. divide \nD. multi\n")
# c = int(input("Enter a second number: "))

# def my_calc(a, b, c):
#     if b == 'A' or b == 'a':
#         b =a + c
#         print(a, '+', c, '=', b )
#     elif b == 'B' or b == 'b':
#         b = a - c
#         print(a, '-', c, '=', b )
#     elif b == 'C' or b == 'c':
#         b = a / c
#         print(a, '/', c, '=', b )
#     elif b == 'D' or b == 'd':
#         b = a * c
#         print(a, '*', c, '=', b )

# my_calc(a, b, c)