# function

# def sum(a, b):
#     a += 1
#     c = a + b
#     # print(c)
#     return c

# res = sum(23,67)
# print(res)
# print(type(sum))

# the shortest function

# def my_fn():
#     pass # used to block error, when it's empty

# print(my_fn()) # None

# --------------------------------------------------------
# Передача неизменяемых объектов в функцию
# def my_nf(a, b):
#     a = a + 1
#     c = a + b
#     return c

# num_one = 10
# num_two = 5

# res = my_nf(num_one, num_two)
# print(res)
# # print(my_nf(num_one, num_two))
# print(num_one)

# --------------------------------------------------------
# Передача изменяемых объектов в функцию
# def increase_person_age(person):
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     return person_copy

# person_one = {
#     'name': 'John',
#     'age': 21,
#     'sex': 'male'
# }

# increase_person_age(person_one)
# new_person_one = increase_person_age(person_one)
# print(new_person_one)
# print(person_one['age'], person_one['name'])
# print(person_one)
# print(dir(dict))

# ---------------------------------------------------------------
# Аргументы функций
# hvis man bruger * så vil man have multi arguments
# def sum_nums(*args):
#     return(sum(args))

# print(sum_nums(2, 3, 4))
# --------------------------------------------------------------
# Аргументы с ключевыми словами
# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     info = f"{person['name']} wrote {person['posts_qty']} posts"
#     return info

# name = input("Enter name: ")
# posts_qty = int(input("Posts you wrote: "))
# # info = get_posts_info(name, posts_qty)
# # print(info)
# print(get_posts_info(name, posts_qty))
# Using arguments with keys words do our code more readeble

# -------------------------------------------------------------------
# Объединение именованых аргументов в словарь
# def get_post_info(**person):
#     print(person)
#     # print(type(person))
#     info = {
#         f"{person['name']} wrote "
#         f"{person['created']} posts"
#     }
#     return info

# info2 = get_post_info(name='Eva', created=25, id=214)
# print(info2)

# ----------------------------------------------------------------------
# Значения параметров функции по умолчанию
# def mult_by_factor(value, multiplier=1):
#     return value * multiplier

# print(mult_by_factor(10, 2))
# print(mult_by_factor(5))
# nalichie znacheniya på default for parametres can using without requiers

# Практика - Значения параметров по умолчанию
# from datetime import date


# def get_weekday():
#     return date.today().strftime('%A')


# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy


# initial_post = {
#     'id': 123,
#     'author': 'Fifa'
# }

# post_with_weekday = create_new_post(initial_post)
# print(initial_post)
# print(post_with_weekday)


# ---------------------------------------------------------------------
# Колбэк функции - Callback function
# Example 1
# def other_fn():
#     pass

# def fn_with_callback(callback_fn):
#     callback_fn()
    
# fn_with_callback(other_fn)

# Example 2
# def print_number_info(num):
#     if (num % 2) == 0:
#         print("Enter number is even")
#     else:
#         print("Enter number is odd")
 
    
# def print_square_num(num):
#     print("Square of the num is", num * num)
    
    
# def process_number(num, callback_fn):
#     callback_fn(num)
 
    
# entered_num = int(input("Enter any number: "))

# process_number(entered_num, print_number_info)
# process_number(entered_num, print_square_num)

# Example 3
def send_data(data):
    """_summary_

    Args:
        data (_type_): _description_
    """  
    # sending data to the remote server
    pass

def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions with updated_data
    send_data_fn(updated_data)
    
process_data({'name': 'Fifa'}, send_data)

# ------------------------------------------------------------
'''
Правила работы с функциями:
- giv navn til functioner efter deres functionalitet
- start functioner med udsagnsord
- en function gør kun en ting
- ikke ændre global variabler til functioner
'''

# ---------------------------------------------------------------
# Документация функции docstring
# - uses to discription for function, classes and module 

# # 1 example
# def mult_by_factor(value, mult=1):
#     """Multiplies number by multiplicator"""
#     return value * mult

# mult_by_factor(5)

# 2 example
# def print_number_info(num):
#     """
#     Prints num information

#     Args:
#         num (int): Integer number

#     Returns:
#         int: Same number
#     """
#     if (num % 2) == 0:
#         print("Num is even")
#     else:
#         print("Num is odd")
#     return num

# print_number_info(34)

# -----------------------------------------------------
# Области видимости

# 1 example
# a = 10

# def my_fn():
#     a = True
#     b = 15
#     print(a)
#     print(b)
    
# my_fn()

# print(a)
# print(b)

# 2 example
# a = 5

# def my_fn():
#     def inner_fn():
#         print(a)
#     inner_fn()
    
# my_fn()

# -------------------------------------------------
# Ключевое слово global в функциях
# a = 5

# def my_glob(): 
#     global a
#     a = 10
    
# my_glob()

# print(a)

# 2 test
# c = 34

# def my_ab(a, b):
#     d = 10
#     print(c)
#     print(a, b)
#     print(dir())

# my_ab(3, 5)

# print(dir())
# print(a) 

# -------------------------------------------------
# Операторы
''' 
comparison (сравнение): + - * /
arithmetic (арифметические): == != < >
logic (логические): not and or
appropriation (присвоение): =
'''
# a = [1, 2]
# b = [1, 2]

# print(a == b)
# print(a.__eq__(b))
# print(a.__eq__)
# print(hex(id(a)))

# --------------------------------------------
# Функция dir
# унарные операторы
''' 
- my_number
+ my_number
not is_activated
'''
# my_num = 10
# print(+ my_num)

# my_bool = True
# # my_bool = False
# print(+my_bool)

# print(not my_num)

# Бинарные операторы
# Binary operator has two operands


# -----------------------------------
# Операторы in, not in
# my_car = {
#     'brand': 'Toyota',
#     'price': 10_000
# }

# print('brand' in my_car)
# print('year' in my_car)
# print('year' not in my_car)

# ----------------------------------
# Ложные значения
'''
dict {}
list []
tuple ()
set set()
range range(0)
str""
'''
# my_list = [1, 2]
# if len(my_list) > 0:
#     print("List has elements")
    
'''
not - prints bool value
and / or - prints one of the value
not not 10 #True
not not 0 #False
not not 'abc' #True
not not '' #False
not not True #True
not not None #False
'''

# -----------------------------------
# Операторы короткого замыкания or и and
# SHORT-CIRCUIT
''' 
AND 
OR
'''
# my_list = [1, 2]
my_list = []    
print(not not my_list)

other_list = ['a', 'b']
print(len(my_list) > 0 or other_list)

my_dict = {}
# my_dict = {'a': 5}
print(bool(my_list and my_dict))

my_list and print("List is not empty")