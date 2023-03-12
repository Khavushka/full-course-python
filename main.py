# Несуществующие ключи и метод get
# my_moto = {
#     'brand' : 'Ducati',
#     'price' : 25000,
#     'engine' : 1.2,
# }

# print(my_moto["engine"])
# print(my_moto.get('engine', 0))


# Кортежи - tuple



print("Hej, her er min egen lommeregner. Enjoy")
a = int(input("Enter a number: "))
b = input("Choose a option: \nA. plus \nB. minus \nC. divide \nD. multi\n")
c = int(input("Enter a second number: "))

def my_calc(a, b, c):
    if b == 'A' or b == 'a':
        b =a + c
        print(a, '+', c, '=', b )
    elif b == 'B' or b == 'b':
        b = a - c
        print(a, '-', c, '=', b )
    elif b == 'C' or b == 'c':
        b = a / c
        print(a, '/', c, '=', b )
    elif b == 'D' or b == 'd':
        b = a * c
        print(a, '*', c, '=', b )

my_calc(a, b, c)