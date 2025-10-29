"""
1. print instruksi
2. minta inputan
3. cek inputan
4. buat mengubah c -> f
5. buat mengubah f -> c
"""
print("Pilihan :")
print("Masukkan 'c' untuk mengubah celcius ke farenheit")
print("Masukkan 'f' untuk mengubah farenheit ke celcius")
UI = input("Masukkan : ").lower()
suhu = float(input("Suhu :"))

if UI == "c":
	print("F = ", 9/5*suhu + 32)
elif UI == "f":
	print("C = ", 5/9*(suhu-32))
else:
	print("Input tidak valid!")