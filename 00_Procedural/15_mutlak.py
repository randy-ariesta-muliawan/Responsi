"""
mutlak -> nilai positif
10 -> 10
-9 -> 9
"""

n = int(input("Masukkan angka : "))
if n >= 0 :
	print(f"Nilai mutlak dari {n} adalah {n}.")
elif n < 0: #else if
	print(f"Nilai mutlak dari {n} adalah {-n}.")