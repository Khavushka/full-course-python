# Task 1
# a = {16, 3, 90}
# a.add(19)

# b = {16, 9, 90, 15}
# c = a & b
# print(c)


# Task 2
# star = range(1,100, 20)
# for i in star:
#     print(i, '*')
#     set_star = i
#     print(set_star)

# Task 3
# vare = ['t-sirt', 'jakke', 'frakke']
# priser = [350, 540, 1200]

# samlet = zip(vare, priser)
# om_dict = dict(samlet)
# print(om_dict)

# samlet = zip(vare, priser)
# om_list = list(samlet)
# print(om_list)

# Task 4
# def merge_lists_to_dict(a, b):
#     c = a + b
#     return c

# fruits = ['apple', 'banana', 'kiwi']
# quantities = [100, 80, 20]

# fruits_q_zip = zip(fruits, quantities)

# om_til_list = list(merge_lists_to_dict(fruits,quantities))
# print(om_til_list)

# Task 5
def merge_lists_to_dict(**fruits):
    print(fruits)
    samlet = {
        f"{fruits['fruit']} //"
        f"{fruits['quantity']} was here"
    }
    return samlet

# fruits_q_zip = zip(fruits, quantities)

# om_til_list = list(merge_lists_to_dict(fruits,quantities))
info2 = merge_lists_to_dict(fruit = ['apple', 'banana', 'kiwi'], quantity = [100, 80, 20] )
print(info2)


# -----------------------------------------------------

def update_car_info(**car):
    pass
        