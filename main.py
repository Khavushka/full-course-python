# Несуществующие ключи и метод get
my_moto = {
    'brand' : 'Ducati',
    'price' : 25000,
    'engine' : 1.2,
}

print(my_moto["engine"])
print(my_moto.get('engine', 0))




