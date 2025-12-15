# mobil = {
# 	{
# 	"merk" : "Honda"
# 	"tipe" : "Civic"
# 	"tahun" : 2018
# 	}
# }

class Mobil:
	def __init__(self, merk, tipe, tahun):
		Mobil.merk = merk
		Mobil.tipe = tipe
		Mobil.tahun = tahun

# my_car = Mobil()
# my_car.merk = "Toyota"
# my_car.tipe = "Kijang"
# print(my_car.merk)
# print(my_car.tipe)
# print(my_car.tahun)

# your_car = Mobil()
# print(your_car.merk)
# print(your_car.tipe)
# print(your_car.tahun)

my_car = Mobil("Toyota", "Innova", 2018)
print(my_car.merk)
print(my_car.tipe)
print(my_car.tahun)

your_car = Mobil("Honda", "civic", 2020)
your_car.tahun = 2020
print(your_car.merk)
print(your_car.tipe)
print(your_car.tahun)