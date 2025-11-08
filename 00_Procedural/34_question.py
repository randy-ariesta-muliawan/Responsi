"""
question_bank (kumpulan pertanyaan)
untuk setiap pertanyaan ditanyakan
diberikan nilai -> benar / total soal x 100
"""

questions = [["Berapa 2 + 2?", "4"],
			["Apa warna langit di hari yang cerah?", "biru"],
			["3 x 4?", "12"]]

benar = 0

for question in questions:
	print(question[0])

	print(question[1])
	jawaban = input("Jawaban : ")
	if question[1] == jawaban :
		print("Benar!")
	else:
		print(f"Salah, jawabannya adalah {question[1]}")

print(f"Nilai anda adalah {benar/len(questions)*100}")