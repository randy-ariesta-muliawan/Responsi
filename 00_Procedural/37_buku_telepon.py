import os
buku_nomor = {
	"Budi" : "0812345678",
	"Suga" : "0813765432",
	"Zaki" : "0898789012"
}

def print_menu():
	os.system("cls")
	print(""" Selamat Datang di Buku Nomor
1. Tambah Nomor Telepon
2. Lihat Isi Buku
3. Hapus Nomor Telepon
4. Cari Nama / Nomor Telepon
5. Keluar
		""")

def cek_pilihan():
	global pilihan
	pilihan = input("Masukkan pilihan (1-5) : ")
	if pilihan == "1":
		tambah_nomor_telepon()
	elif pilihan == "2":
		lihat_isi_buku()
	elif pilihan == "3":
		hapus_nomor()
	elif pilihan == "4":
		cari_nomor()
	elif pilihan == "5":
		pass
	else:
		print("Input tidak Valid")

def tambah_nomor_telepon():
	os.system("cls")
	print("--- Tambah Nomor Telepon ---")
	nama = input("Masukkan Nama Kontak :")
	nomor = input("Masukkan Nomor Kontak :")
	print(f"Nama = {nama}, Nomor = {nomor}")
	setuju = input("Apakah anda setuju untuk menyimpan kontak ini? (Y/N)")
	if setuju == "Y":
		buku_nomor[nama] = nomor
		print("Kontak berhasil disimpan!")

def lihat_isi_buku():
	os.system("cls")
	print("--- Isi Buku Nomor ---")
	for kontak in buku_nomor:
		print("Nama\t :", kontak)
		print("Nomor\t :", buku_nomor[kontak])
	input("tekan ENTER untuk melanjutkan ...")

def hapus_nomor():
	os.system("cls")
	print("--- Hapus Nomor Telepon ---")
	nama = input("Masukkan nama kontak yang ingin dihapus :")
	if nama in buku_nomor:
		setuju = input("Apakah anda yakin untuk menghapus kontak ini?(Y/N)")
		if setuju:
			del buku_nomor[nama]
	else:
		print("Kontak tidak ditemukan")

def cari_nomor():
	os.system("cls")
	print("--- Cari Nomor Telepon ---")
	nama = input("Masukkan nama kontak yang ingin dicari :")
	if nama in buku_nomor:
		print(f"Nama = {nama}")
		print(f"Nomor = {buku_nomor[nama]}")
	else:
		print("Kontak Tidak Ditemukan")
	input("tekan ENTER untuk melanjutkan ...")


pilihan = None
while pilihan != "5":
	print_menu()
	cek_pilihan()