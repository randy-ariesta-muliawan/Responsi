# try: # Mencoba
# 	a = int(input())
# 	b = int(input())
# except ValueError: # Kalau ada error
# 	print("Masukkan angka bulat")
# else: # Kalau tidak error
# 	print(a + b)
# finally: # Lakukan
# 	print("Done!")

while True:
	try: # Mencoba
		a = int(input())
		b = int(input())
	except ValueError: # Kalau ada error
		print("Masukkan angka bulat")
	else: # Kalau tidak error
		print(a + b)
	finally: # Lakukan
		print("Done!")