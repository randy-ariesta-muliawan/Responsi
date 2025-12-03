class Mobil:
	def __init__(self, merk, tipe, tahun):
		self.merk = merk
		self.tipe = tipe
		self.tahun = tahun
		self.odometer = 0

	def describe_a_car(self): # Method
		print(f"This car is a {self.merk} {self.tipe} car from {self.tahun}.")

	def jalan(self, km):
		self.odometer += km


my_car = Mobil("toyota", "innova", "2021")
print(my_car.merk)
my_car.describe_a_car()

print(my_car.odometer)
my_car.jalan(20)
print(my_car.odometer)


your_car = Mobil("honda", "civic", "2000")
your_car.describe_a_car()

print(your_car.odometer)
your_car.jalan(100)
print(your_car.odometer)

your_car.merk = "toyota"
your_car.describe_a_car()