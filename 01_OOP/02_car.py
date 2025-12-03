class Mobil:
	def __init__(self, merk, tipe, tahun):
		self.merk = merk
		self.tipe = tipe
		self.tahun = tahun

	def describe_a_car(self): # Method
		print(f"This car is a {self.merk} {self.tipe} car from {self.tahun}.")


my_car = Mobil("toyota", "innova", "2000")
print(my_car.merk)
my_car.describe_a_car()