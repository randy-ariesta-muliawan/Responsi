jumlah = 0
banyak_angka = int(input("Berapa banyak angka yang ingin dirata-ratakan?"))
counter = 0

while counter < banyak_angka :
	counter +=1
	angka = float(input(f"Masukkan angka ke-{counter} : "))
	jumlah += angka
print("Rata-ratanya adalah : ", jumlah/banyak_angka)

# 2,5,4
"""
2 + 5 + 4 = 11
11/3 = 3.666