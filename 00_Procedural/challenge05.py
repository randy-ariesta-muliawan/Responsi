"""
Buat Program Pembuat Pizza:
ada function buat pizza dengan args(*) --> topping

print("Making a pizza with :")
- topping1
- topping2

Kalo tidak ada topping,
print("Tidak ada topping")

"""
from os import system

def make_pizza(*topping):
	system("clear")
	print("Making a pizza with:")
	for toppings in topping:
		print(f" - {toppings}")

def make_pizza2(*topping):
	print("\nMaking a pizza with:")
	for toppings in topping:
		print(toppings)

make_pizza('sosis', 'keju', 'jamur')
make_pizza2('Tidak ada topping')