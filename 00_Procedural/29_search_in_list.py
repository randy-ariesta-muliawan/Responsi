makanan = ["burger", "pempek", "permen", "tekwan", "nasi"]
dicari = input("Masukkan makanan yang dicari : ")

if dicari in makanan :
	print(f"{dicari} ada!")
else:
	print(f"{dicari} tidak ada!")


index = 0
while index < len(makanan) :
	if dicari == makanan[index]:
		print(f"{dicari} ada!")
		# break
		exit()
		