from os import system
# Buatlah program yang jika dijalankan memberikan instruksi berikut:

# Selamat datang di program penghitung luas!
# [1] Luas persegi # sisi
# [2] Luas persegi_panjang # panjang, lebar
# [3] Luas segitiga # alas, tinggi
# [4] Luas lingkaran # jari-jari
# [Q] Keluar

#Loop
def print_instruksi():
	system("cls")
	print("[1] Luas persegi")
	print("[2] Luas persegi panjang")
	print("[3] Luas segitiga")
	print("[4] Luas lingkaran")
	print("[Q] Keluar")
	

def luas_persegi():
	sisi_p = float(input("Sisi :"))
	print("Hasil", sisi_p*sisi_p)

def luas_persegi_panjang():
	panjang_persegi_p = float(input("Panjang :"))
	lebar_persegi_p = float(input("Lebar :"))
	print("Hasil :", panjang_persegi_p * lebar_persegi_p)

def luas_segitiga():
	alas = float(input("Alas :"))
	tinggi = float(input("Tinggi :"))
	print("Hasil", (alas * tinggi) / 2)

def luas_lingkaran():
	radius = float(input("Jari-jari :"))
	print("Hasil :", 3.14 * radius * radius)
	
def cek_respon(char):
	system("cls")
	if char == "1":
		luas_persegi()
	elif char == "2":
		luas_persegi_panjang()
	elif char == "3":
		luas_segitiga()
	elif char == "4":
		luas_lingkaran()
	else:
		print("Input tidak valid!")
	input("tekan ENTER untuk melanjutkan ...")



def main():
	char = None
	while char != 'q':
		print_instruksi()
		char=input("Masukkan :")
		if char == "q":
			break
		cek_respon(char)


if __name__ == "__main__":
	main()