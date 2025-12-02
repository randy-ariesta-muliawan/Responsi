# mobil = {
# 	"merk" : "toyota"
# 	"tipe" : "innova"
# 	"tahun" : 2000
# }

class Mobil:
	def __init__(self, merk, tipe, tahun):
		self.merk = merk
		self.tipe = tipe
		self.tahun = tahun


my_car = Mobil("toyota", "innova", "2000")
print(my_car.merk)
