"""
1. Minta username
2. Minta password
3. Cek username
4. Cek password
"""
username = input("Username: ").lower()
password = input("Password: ")
if username == "Randy".lower() and password == "abcd123" :
	print("Welcome Randy!")
elif username == "Nadya".lower() and password == "123456" :
	print("Welcome Nadya")

else:
	print("Tidak dikenal!")


print("AbcDef".upper())
print("AbcDef".lower())