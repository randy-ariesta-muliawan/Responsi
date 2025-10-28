# local variable
# global variable

a = 4 # global variable

def tulis_a():
	a = 17 # local variable
	print("A di dalam function :", a)

tulis_a()
print('A diluar function', a)


var1 = 20
var2 = 30

def tambah_variable() :
	var3 = 100 # local variable
	print(var1)
	print(var2)
	print(var3)

tambah_variable()
print(var1)
print(var2)
print(var3)