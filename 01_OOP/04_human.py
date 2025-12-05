class Eye:
	def __init__(self, color, illness):
		self.color = color
		self.illness = illness

class Hair:
	def __init__(self, color, curly):
		self.color = color
		self.curly = curly

class Human:
	def __init__(self, name, gender, height, eye_color, eye_illness, hair_color, hair_curly = True):
		self.name = name
		self.gender = gender
		self.height = height
		self.eye = Eye(eye_color, eye_illness)
		self.hair = Hair(hair_color, hair_curly)

	def describe_me(self):
		print(f"Hello, I am {self.name}. I am a {self.gender}. I am {self.height}cm. I have {self.eye.color} eye with {self.eye.illness} illness and {self.hair.color} {self.hair.curly} hair")


Budi = Human("Budi", "male", 195, "brown", None, "black", "curly")
Budi.describe_me()

Sutejo = Human("Sutejo", "female", 293, "red", "-1.0", "dark red", "straight")
Sutejo.describe_me()

Ani = Human(name = "Ani", gender = "female", eye_color = "brown", height = "198", hair_color = "green", hair_curly = "curly", eye_illness = None)
Ani.describe_me()