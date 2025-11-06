numbers = [4, 5, 7, 8, 9, 1, 0, 7, 10]
numbers.sort()

sebelum = None

print(numbers)
for sekarang in numbers:
	print("sekarang = ",sekarang, "sebelum = ", sebelum)
	if sebelum == sekarang :
		print(f"Ada double angka {sekarang}.")
	
	sebelum = sekarang