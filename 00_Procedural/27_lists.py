makanan_favorit1 = "ayam goreng", "a", "b"
makanan_favorit2 = "permen"
makanan_favorit3 = "burger"
# ...

# Membuat list 1
makanan_favorit = ["ayam_goreng", "permen", "burger", "pizza", "lolipop"]
#index 					0			 1 		  2 		 4

print(makanan_favorit[2])

# Membuat list 2
film_favorit = list(makanan_favorit1)
print(film_favorit)

# Mengganti isi list
makanan_favorit[0] = "pempek"
print(makanan_favorit)

# Menambah isi list
makanan_favorit.append("rendang")
print(makanan_favorit)

# Melihat banyak isi list
banyak = len(makanan_favorit)
print(banyak)
my_string = "abc12345"
print(len(my_string))

# Menghapus isi list
# Cara 1
del makanan_favorit[2] # index
print(makanan_favorit)

# Cara 2
makanan_favorit.pop(0) # index
print(makanan_favorit)

# Cara 3
makanan_favorit.remove("lolipop")
print(makanan_favorit)

# Memasukkan data
makanan_favorit.insert(1, "kentang goreng")
print(makanan_favorit)

# Mengurutkan list
# Permanen
film_favorit = ["avenger", "star wars", "frozen"]
print(film_favorit)
film_favorit.sort()
print(film_favorit)

# Sementara
print(makanan_favorit)
print(sorted(makanan_favorit))
print(makanan_favorit)