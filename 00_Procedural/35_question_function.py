questions = [["Berapa 2 + 2?", "4"],
			["Apa warna langit di hari yang cerah?", "biru"],
			["3 x 4?", "12"]]

def cek_jawaban(jawaban, inputan):
	if jawaban == inputan:
		return True
	else:
		return False

def print_questions():
	global benar
	for question in questions:
		print(question[0])
		jawaban = input("Jawaban : ")
		
		correct = cek_jawaban(question[1], jawaban)
		if correct:
			print("Benar")
			benar += 1
		else:
			print("Salah")

def print_nilai(total_soal, benar):
	nilai = benar/total_soal*100
	print(f"Nilai anda {nilai}")

benar = 0

print_questions()
print_nilai(len(questions), benar)