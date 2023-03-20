# Встроенная функция zip

fruits = ['apple', 'banana', 'kiwi']
quantities = [100, 80, 20]

fruits_q_zip = zip(fruits, quantities)
# fruits_q_zip = (fruits, quantities)
# print(fruits_q_zip)
om_til_list = list(fruits_q_zip)
print(om_til_list)

# Конвертация zip в dict
# om_til_dict = dict(fruits_q_zip)
# print(om_til_dict)