angka = float(input("Masukkan angka"))
"""
genap = angka/2 (sisa 0)
ganjil = angka/2 (sisa 1)
"""
if angka %2 == 0:
	print("Angkanya genap")
elif angka%2 == 1:
	print("Angkanya ganjil")
else:
	print("Angkanya aneh.")