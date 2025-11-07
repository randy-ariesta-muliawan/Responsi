#makanan_favorit = ["ayam_goreng", "permen", "burger", "pizza", "lolipop", []]
favoritku = [["ayam_goreng", "permen", "burger", "pizza", "lolipop"], ["avenger", "star wars", "frozen"]]

print(favoritku[0][1])
# for favorit in favoritku:
#     print(favorit)

favoritku = [
	["ayam_goreng", "permen", "burger", "pizza", "lolipop"],
	["avenger", "star wars", "frozen"]
]
favoritku.append(["gucci", "uniqlo", "H&M"])
print(favoritku)
favoritku[0].append("pempek")
print(favoritku)