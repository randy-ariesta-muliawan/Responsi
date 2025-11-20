import json
import random

def save_data(angka):
	with open("data.json", "w") as file:
		json.dump(angka, file)
	print("Oke, aku akan ingat")

try:
	with open("data.json", "r") as file:
		angka = json.load(file)
except:
	tebakan = random.randint(0, 100)
	masukan = input(f"Apakah angka favoritmu adalah {tebakan}? (Y/N)")
	if masukan.upper() == "Y":
		save_data(tebakan)
	else:
		angka = input("Berapakah angka favoritmu?")
		save_data(angka)

else:
	print("Angka favoritmu adalah", angka)
"""
Challenge
Jika angka favorit belum ada, program akan menebak angka (secara random) dari 0-100 dan akan meminta konfirmasi (Y/N) dari pengguna

Jika Y, program akan menyimpan angkanya
Jika N, program akan menanyakan angka favorit pengguna dan menyimpan angkanya
"""