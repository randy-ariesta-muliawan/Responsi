with open("data.txt", "r") as file:
	buah_favorit = file.readlines()

print(buah_favorit)
buah_favorit_bersih = []
for buah in buah_favorit:
	buah_favorit_bersih.append(buah.strip())
print(buah_favorit_bersih)