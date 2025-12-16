class Dog:
	def __init__(self, name="NoName", race="NoRace", age=0): # fungsi konstruktor
		self.name = name
		self.race = race
		self.age = age
		self.favorite_food = "Dog Food"

	def sleep(self, hour): # method
		print(f"{self.name} is sleeping for {hour} hour(s)")

	def eat(self, food):
		if food == self.favorite_food:
			print(f"{self.name} is eating {food} and he/she likes it")
		else:
			print(f"{self.name} is eating {food} and he/she doesn't it")


lexa = Dog("Lexa", "shitzu", 1)
lexa.sleep(2)
lexa.eat("Dog Food")
lexa.eat("Rice")
# print(lexa.name)
# print(lexa.race)
# print(lexa.age)