from abc import ABC, abstractmethod, abstractproperty

class Person(ABC):
	def __init__(self, name):
		self.__name = name
		
	@abstractproperty 
	def gpa(self): 
		return "parent class"
		
	@abstractmethod
	def dowork(self): 
		pass
		
	@property
	def name(self):
		return self.__name
		
	def display(self):
		print('Person:', self.name)
		
class Student(Person):
	def __init__(self, name, gpa):
		super().__init__(name)
		self.__gpa = gpa
	
	@property
	def gpa(self):
		return self.__gpa
	
	def dowork(self):
		print("Doing homework!")
		
	def display(self):
		super().display()
		print('Student:', self.gpa)
		
def main():
	# p = Person()    # can't create a Person object
	a = Student('Peter', 3.8)
	a.dowork()
	a.display()

main()
