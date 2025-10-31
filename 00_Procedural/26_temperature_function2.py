import os
"""
1. print instruksi
2. minta inputan
3. cek inputan
4. buat mengubah c -> f
5. buat mengubah f -> c
"""
def print_instruksi():
	os.system("cls") # mac/linux = clear
	print("Pilihan :")
	print("Masukkan 'c' untuk mengubah celcius ke farenheit")
	print("Masukkan 'f' untuk mengubah farenheit ke celcius")
	print("Masukkan 'q' untuk keluar")

def minta_input():
	UI = input("Masukkan : ").lower()
	if UI == "q":
		return UI, None
	suhu = float(input("Suhu :"))
	return UI, suhu #Lokal

def cek_input(UI, suhu):
	if UI == "c":
		print("F = ", 9/5*suhu + 32)
	elif UI == "f":
		print("C = ", 5/9*(suhu-32))
	else:
		print("Input tidak valid!")
	input("tekan ENTER untuk melanjutkan ...")

def main():
	UI = None #Lokal
	suhu = None #Lokal
	while UI != 'q':
		print_instruksi()
		UI, suhu = minta_input()
		if UI == "q":
			break
		cek_input(UI, suhu)


if __name__ == "__main__":
	main()