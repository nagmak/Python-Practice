class Person:
	def __init__(self, name):
		# created a new field called name
		self.name = name
		#self.name is a local variable
		# where name is a part of the self object

	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()