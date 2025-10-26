"""
f(x) = x+1

x = parameter
f(x) = def
x+1 = isi function

f(1) = 1 + 1 = 2
"""

def hello() :
	print("Hello everyone")
	print("What a lovely day!")

hello()

def luas(panjang, lebar):
	print("Luas = ", panjang*lebar)

luas(3,2) # 3,2 -> argumen

def luas_segitiga(alas, tinggi) :
	luas = alas*tinggi/2
	return luas

l_segitiga = luas_segitiga(5,2)
print(l_segitiga)

l_segitiga2 = luas_segitiga(6,3)
print(l_segitiga2)