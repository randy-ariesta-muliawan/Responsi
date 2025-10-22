"""
1. Berikan angka yang ingin ditebak
2. Kita minta user memasukkan angka tebakan
3. Kita cek angka tebakan sama atau tidak dengan yang dimasukkan user
4. Apabila sama, Benar
5. Apabila tidak, angka tebakan >, kebesaran
6. Apabila tidak, angka tebakan <, kekecilan
"""
angka = 35
tebakan = None

print("Tebaklah Angka!")
while angka != tebakan :
	tebakan = int(input("Angkanya adalah ..."))

	if tebakan == angka :
		print("Benar")
	elif tebakan > angka :
		print("Kebesaran")
	elif tebakan < angka :
		print("Kekecilan")