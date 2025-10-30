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
	global UI, suhu
	UI = input("Masukkan : ").lower()
	if UI == "q":
		return
	suhu = float(input("Suhu :"))

def cek_input():
	global UI, suhu
	if UI == "c":
		print("F = ", 9/5*suhu + 32)
	elif UI == "f":
		print("C = ", 5/9*(suhu-32))
	else:
		print("Input tidak valid!")
	input("tekan ENTER untuk melanjutkan ...")

UI = None
while UI != 'q':
	print_instruksi()
	minta_input()
	if UI == "q":
		break
	cek_input()