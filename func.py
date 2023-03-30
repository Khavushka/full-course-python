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
def get_post_info(**person):
    print(person)
    # print(type(person))
    info = {
        f"{person['name']} wrote "
        f"{person['created']} posts"
    }
    return info

info2 = get_post_info(name='Eva', created=25, id=214)
print(info2)

# ----------------------------------------------------------------------
# Значения параметров функции по умолчанию
def mult_by_factor(value, multiplier=1):
    return value * multiplier

print(mult_by_factor(10, 2))
print(mult_by_factor(5))
# nalichie znacheniya på default for parametres without requiers


