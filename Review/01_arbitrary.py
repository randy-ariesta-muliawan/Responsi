def buat_pizza(*topping): # *args = arbitrary argument
	print(f"Sedang membuat pizza dengan topping:")
	for topping in toppings:
		print("-", topping)

def buat_pizza2(**spesifikasi): # *kwargs = key word arbitrary argument
	print(f"Sedang membuat pizza dengan :")
	for key, value in spesifikasi.items():
		print(f"{key} : {value}")

def buat_pizza3(spicy=False, *toppings, **notes):
	if spicy:
		print("Membuat spicy pizza dengan :")
	else:
		print("Membuat pizza dengan :")

	print("Topping :")
	for topping in toppings :
		print("-", topping)

	print("Notes :")
	for key, value in notes.items():
		print(f"{key} : {value}")

# buat_pizza(topping = "pepperoni", pinggiran = "nugget")
buat_pizza3(True, "pepperoni", "keju", "jamur", note_pinggiran = "Pinggiran mau nugget", note_pinggiran2 = "pinggiran jangan keras")