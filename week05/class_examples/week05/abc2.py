from abc import ABC, abstractmethod, abstractproperty

class Parent(ABC):
	@abstractmethod
	def dowork(self): 
		pass
		
	@abstractmethod
	def make_money(self): 
		pass
		
class Child(Parent):
	def dowork(self):
		print("Learn computer programming!")
		
class GrandChild(Child):
	def make_money(self):
		print("Stock trading!")
		
def main():
	# TypeError: Can't instantiate abstract class Parent with abstract methods dowork, make_money
	# p = Parent()    
	
	# TypeError: Can't instantiate abstract class Child with abstract methods make_money
	# c = Child()
	
	g = GrandChild()
	g.dowork()
	g.make_money()
	

main()
