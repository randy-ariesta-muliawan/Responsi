
tebakan = input("Masukkan nama yang ingin ditebak : ")
nama = "Budi"
counter = 1

while counter != 3 :
	if tebakan.upper() != nama.upper():
		print(f"Nama {tebakan} bukan nama yang benar")
		tebakan = input("Masukkan nama yang ingin ditebak : ")
		counter += 1
	
	else:
		print(f"Nama {nama} benar")
		counter = 3


else:
	print(f"Jawaban yang benar adalah {nama} ")

"""
print("Tebak Nama!")
count = 0
nama = "Randy"
while count < 3 :
	tebakan = input("Masukkan tebakan : ")
	count += 1
	if tebakan == nama :
		print("Tebakan benar!")
		berhasil = True
		exit()
		#break

if not berhasil:
	print(f"Anda gagal! Jawabannya adalah {nama}")
"""
