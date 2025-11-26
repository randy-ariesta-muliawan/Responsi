angka = 0
jumlah = 0
print("Masukkan angka baru ke dalam jumlah !")
print("Masukkan q untuk keluar")
while angka != "q" :
	jumlah += float(angka)
	print("Jumlah angka sekarang", jumlah)
	angka = input("Masukkan angka : ")
	
print("Jumlah angka = ", jumlah)