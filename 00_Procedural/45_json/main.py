import json

with open("data.json", "w") as file:
	makanan = ["pempek", "model", "kentang"]
	json.dump(makanan, file) # apa yang ingin dimasukkan, nama file

with open("data.json", "r") as file:
	makanan2 = json.load(file)

print(makanan2)