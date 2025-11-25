angka = 1
jumlah = 0

x = True

print("Masukkan angka baru ke dalam jumlah !")
print("Masukkan angka 0 atau huruf q untuk keluar")
while x == True:
	print("Jumlah angka sekarang", jumlah)
	angka = input("Masukkan angka : ")
	if angka != "q":
		angka = int(angka)
		jumlah += angka
	else:
		x = False
print("Jumlah angka = ", jumlah)