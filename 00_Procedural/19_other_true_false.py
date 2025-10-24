"""
True:			False:
True 			False
1 				0

int, selain 0 	None
"1eqwdc"		""
[a,b,c]			[]
{"1" : "1"}		{}
"""

print(bool(True))
print(bool(1))
print(bool(123))
print(bool("abc"))
print(bool([1,2,3]))
print(bool({"1" : "1"}))
print()
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))
print(bool({}))

UI = input()
# if bool(UI) == False:
# 	print("Tidak ada input")
# elif bool(UI) == True :
# 	print(UI)
if bool(UI):
	print("Ada input")