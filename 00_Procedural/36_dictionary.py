favoritku = {"makanan" : "ayam goreng", 
			"minuman" : "es jeruk"}

print(favoritku["makanan"])

# Menambahkan item
print(favoritku)
favoritku["film"] = "squid game"
print(favoritku)

# Menghapus

del favoritku["minuman"]
print(favoritku)

# Mengganti
favoritku["makanan"] = "indomie"
print(favoritku)

print(len(favoritku))