class Student:
	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa
		
	def dowork(self):
		print('Student', self.name, 'doing homework.')
		
	def display(self):
		print('name =', self.name)
		print('gpa =', self.gpa)
		
class Teacher:
	def __init__(self, name, salary, project):
		self.name = name
		self.salary = salary
		self.project = project
		
	def dowork(self):
		print('Teacher', self.name, 'teaching a class.')
		
	def display(self):
		print('name =', self.name)
		print('salary =', self.salary)
		print('project =', self.project)
		
class TA(Teacher, Student):
	def __init__(self, name, gpa, salary, project):
		Teacher.__init__(self, name, salary, project)
		Student.__init__(self, name, gpa)
		
	def dowork(self):
		super().dowork()
		print('TA', self.name, 'grading homework.')
		
	def display(self):
		super().display()
		
def main():
	ta = TA('Peter', 3.8, 1000, 'MAX5')
	ta.dowork()
	ta.display()
	
main()
