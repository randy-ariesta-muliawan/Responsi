a = 20
b = -12

if a < 0:
	a = -a
if b < 0:
	b = -b

print("Nilai mutlak dari a = ", a)
print("Nilai mutlak dari b = ", b)

c = 18
d = -29

def mutlak(n): #parameter
	if n < 0 :
		n = -n
	print("Nilai mutlaknya adalah =", n)

mutlak(c) # argumen
mutlak(d)
mutlak(-24)
mutlak(10)