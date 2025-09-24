'''
Question:
Implement the following classes according to the class diagrams. And you should add appropriate getters and 
setters using @property decorator if necessary.
You are required to define function parameters for the Group constructor (?), ITGroup constructor (?) 
Programmer constructor (?), and Manager constructor (?) in order to create objects of them properly.
● All classes need to implement display method.
● Annual Income = salary * 12 + bonus if any.
● After you implement all the classes and the methods specified in the class diagram, write a main 
method to create objects of the classes you defined, test their methods and print out their contents.
The below is the method to test your classes:
def main() -> None:
p1: Programmer = Programmer("Lily", "C++, Java", 10000)
p2: Programmer = Programmer("Judy", "Python, Java", 18000)
m: Manager = Manager("Peter", "Management", 20000, 20000)
proj1: Project = Project("MAX-5", 200000, True)
proj2: Project = Project("FOX-4", 100000, False)
proj3: Project = Project("FOX-XP", 500000, True)
itgrp: ITGroup = ITGroup("ATX Group")
itgrp.add_member(p1)
itgrp.add_member(p2)
itgrp.add_member(m)
itgrp.add_project(proj1)
itgrp.add_project(proj2)
itgrp.add_project(proj3)
itgrp.display()
p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
itgrp.add_member(p3)
itgrp.ask_anyone_dowork()
print()
itgrp.ask_manager_dowork()
print("\nGet the largest project...")
maxProj: Optional[Project] = itgrp.find_largest_project()
if maxProj is not None:
maxProj.display()
print("\nGet the acive projects...")
projects: list[Project] = itgrp.get_active_projects()
for proj in projects:
proj.display()
print()
itgrp.display()
itgrp.remove_member(p3.name)
print("\nGet the members with high income...")
members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
for member in members:
member.display()
print()
if __name__ == "__main__":
main()
The expected output is:
The group has these members:
name = Lily
skills = C++, Java
salary = 10000
name = Judy
skills = Python, Java
salary = 18000
name = Peter
skills = Management
salary = 20000
bonus = 20000
The group has these projects:
projname = MAX-5
budget = 200000
active = True
projname = FOX-4
budget = 100000
active = False
projname = FOX-XP
budget = 500000
active = True
Programmer Lily is writing a program.
Programmer Judy is writing a program.
Manager Peter is supervising a team of programmers.
Programmer Jone is writing a program.
Manager Peter is supervising a team of programmers.
Get the largest project...
projname = FOX-XP
budget = 500000
active = True
Get the acive projects...
projname = MAX-5
budget = 200000
active = True
projname = FOX-XP
budget = 500000
active = True
The group has these members:
name = Lily
skills = C++, Java
salary = 10000
name = Judy
skills = Python, Java
salary = 18000
name = Peter
skills = Management
salary = 20000
bonus = 20000
name = Jone
skills = Python, Java
salary = 1118000
The group has these projects:
projname = MAX-5
budget = 200000
active = True
projname = FOX-4
budget = 100000
active = False
projname = FOX-XP
budget = 500000
active = True
Get the members with high income...
name = Judy
skills = Python, Java
salary = 18000
name = Peter
skills = Management
salary = 20000
bonus = 20000

'''


class Person:
    def __init__(self, name) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f"name: {self.__name}" 
    
    def display(self) -> None:
        print(self)
        
    def dowork(self) -> None:
        print(f"Person:  {self.__name} is doing nothing")
        
    @property
    def name(self) -> str:
        return self.__name
    
    

    

class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n, skills: {self.__skills}\n, salary: {self.__salary}\n"
    
    def dowork(self) -> None:
        print(f"Programmer: {self.name} is writing a program")
        
    def get_annual_income(self) -> float:
        return self.__salary * 12
    
    @property
    def salary(self) -> float:
        return self.__salary
    @property
    def skills(self) -> str:
        return self.__skills
class Manager(Programmer):
    def __init__(self, name : str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)      
        self.__bonus = bonus
    def __str__(self) -> str:
        return f"{super().__str__()}\n, bonus: {self.__bonus}"
    @property
    def bonus(self) -> float:
        return self.__bonus
    
    def dowork(self) -> None:
        print(f"Manager {self.name} is supervising a team of programmers.")
        
    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus


class Group:
    
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members: list[Person] = []
        
    def add_member(self, member: Programmer) -> None:
        self.__members.append(member)
        
    def remove_member(self, name: str) -> None:
        # for membr in self.__members:
        #     if membr == name:
        #         self.__members.remove(membr)
        #         break
        
        i = 0
        while i < len(self.__members):
            if self.__members[i].name == name:
                self.__members.pop(i)
            else:
                i += 1
        
    def __str__(self) -> str:
        output = "The group  has these members:\n"
        for member in self.__members:
            output += f"name = {member.name}\n"
            if isinstance(member, Programmer):
                
                output += f"skills = {member.skills}\n"
                output += f"salary = {member.salary}\n"
                if isinstance(member, Manager):
                    output += f"bonus = {member.bonus}\n"
        return output
    def display(self) -> None:
        print(self)
        
    def ask_manager_dowork(self) -> None:
        for membr in self.__members:
            if isinstance(membr, Manager):
                membr.dowork()
    def get_allMembers_morethan(self, income: float) -> list[Programmer]:
        high_members: list[Programmer] = []
        for member in self.__members:
            if isinstance(member, Programmer):
                if member.get_annual_income() > income: 
                   high_members.append(member)
        return high_members
    def ask_anyone_dowork(self) -> None:
        for membr in self.__members:
            membr.dowork()
    
    
class Project:
    def __init__(self, projname: str, budget= 0.0 , active = False) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active
        
    def __str__(self) -> str:
        return f"Project name: {self.__projname}, budget: {self.__budget}, active: {self.__active}"
    
    def display(self) -> None:
        print(self)
        
    @property
    def projname(self) -> str:
        return self.__projname
    
    @property
    def budget(self) -> float:
        return self.__budget
    
    @property
    def active(self) -> bool:
        return self.__active            
        

class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects: list[Project] = []
    
    def add_project(self, project: Project) -> None:
        self.__projects.append(project)
        
    def __str__(self) -> str:
        
        members_output = super().__str__()
        
        
        output = "The group has these projects:\n"
        for project in self.__projects:
            output += f"projectname = {project.projname}\n"
            output += f"budget = {project.budget}\n"
            output += f"active = {project.active}\n"
            
        return members_output + '\n' +output
    def find_largest_project(self) -> Project:
        max_proj: Project = self.__projects[0]
        for proj in self.__projects:
            if proj.budget > max_proj.budget:
                max_proj = proj
        return max_proj
    def display(self) -> None:
        print(self)
        
    def get_active_projects(self) -> list[Project]:
        active_projects: list[Project] = []
        for proj in self.__projects:
            if proj.active:
                active_projects.append(proj)
        return active_projects
    
def main():
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 10000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    # itgrp: Group = Group("ATX Group")
    # itgrp.add_member(p1)
    # itgrp.add_member(p2)
    # itgrp.add_member(p1)
    # itgrp.add_member(m)
    # itgrp.add_member(p1)
    # itgrp.add_member(p1)
    # print(itgrp)
    # itgrp.display()
    # # print("After removing .......")
    # itgrp.remove_member("Lily")
    # print(itgrp)
    
    # itgrp.ask_manager_dowork()
    
    # members: list[Programmer] = itgrp.get_allMembers_morethan(20000)
    # for membr in members:
    #     membr.display()
    # print()
    
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)
    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()
    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)
    itgrp.ask_anyone_dowork()
    print() 
    itgrp.ask_manager_dowork()
    print("\nGet the largest project...")
    maxProj: Optional[Project] = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()
    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
    print()
    itgrp.display()
    itgrp.remove_member(p3.name)
    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
    for memeber in members:
        memeber.display()
    print() 
    
    
    

    
    
if __name__ == "__main__":
    main()
    
