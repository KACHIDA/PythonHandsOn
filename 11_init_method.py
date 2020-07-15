"""
__init__ method - this method is run as soon as an object of a class in instantiated (i.e, created). The Method is useful to do any initialization (i.e, passing initial values to your object) you want to do with your object. Notice that double underscore both at begining and end of the name.

"""

class Person:
	def __init__(self,name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is ', self.name)

p = Person('Kanna')
p.say_hi()

