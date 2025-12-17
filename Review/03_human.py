class Hair:
	def __init__(self, color, curly):
		self.color = color
		self.curly = curly

class Eye:
	def __init__(self, color, illness):
		self.color = color
		self.illness = illness

class Human:
	def __init__(self, name, age, gender, height, eye_color, eye_illness,hair_color, hair_curly):
		self.name = name
		self.age = age
		self.gender = gender
		self.height = height
		self.eye = Eye(eye_color, eye_illness)
		self.hair = Hair(hair_color, hair_curly)

	def describe_me(self):
		print(f"Hello my name is {self.name}. I am {self.age} years old {self.gender}. I am {self.height} cm. I have {self.eye.color} eyes with {self.eye.illness} illness and {self.hair.color} {self.hair.curly} hair.")

Anton = Human("Anton Antonius", 13, "Male", 150, "brown", "miopi -1.0", "black", "straight")
Anton.describe_me()