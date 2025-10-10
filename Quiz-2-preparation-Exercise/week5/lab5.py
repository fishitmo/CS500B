class Person:
    def __init__(self, name) -> None:
        self.__name = name
        
    def __str__(self) -> str:
        return f"name: {self.__name}"
    def display(self):
        print(self)
        
    def dowork(self):
        print(f"Person: {self.__name} is doing nothing")
    
    @property
    def name(self):
        return self.__name
    
    
class Programmer(Person):
    def __init__(self,name: str, skills: str, salary: float ) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary
    
    def get_annual_income(self) -> float:
        return self.__salary * 12 
        
    def display(self) -> None:
        super().display()
        print(f"skills: {self.__skills}")
        print(f"salary: {self.__salary}")
        
    @property
    def skills(self) -> str:
        return self.__skills
        
    @property
    def salary(self) -> float:
        return self.__salary
        
    def dowork(self) -> None:
        print(f"Programmer: {self.name} is writing a program")
    
    
class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self.__bonus = bonus
        
    @property
    def bonus(self) -> float:
        return self.__bonus
        
    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus
    
    def display(self) -> None:      
        super().display()
        print(f"bonus: {self.__bonus}")
        
    def dowork(self) -> None:
        print(f"Manager: {self.name} is supervising a team of programmers.")
        
    
class Group:
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members: list[Person] = []
        
    def add_member(self, memeber: Person) -> None:
        self.__members.append(memeber)
        
    def remove_member(self, name: str) -> None:
        
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
    
    def ask_anyone_dowork(self) -> None:
        for member in self.__members:
            member.dowork()
            
    def ask_manager_dowork(self) -> None:
        for member in self.__members:
            if isinstance(member, Manager):
                member.dowork()
    
    def get_allMembers_morethan(self, income: float) -> list[Programmer]:
        high_members: list[Programmer] = []
        for member in self.__members:
            if isinstance(member, Programmer):
                if member.get_annual_income() > income: 
                   high_members.append(member)
        return high_members
    
    def display(self) -> None:
        print(self)
        
    
class Project:
    def __init__(self, projname: str, budget= 0.0 , active = False) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active
    @property
    def projname(self) -> str:
        return self.__projname
        
    @property
    def budget(self) -> float:
        return self.__budget
        
    @property
    def active(self) -> bool:
        return self.__active
        
    def __str__(self) -> str:
        return f"Project name: {self.__projname}, budget: {self.__budget}, active: {self.__active}"
        
    def display(self) -> None:
        print(self)
        
        
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
        return output
    
    def display(self) -> None:
        print(self)
        
    def find_largest_project(self) -> Project:
        largest_project: Project = self.__projects[0]
        for project in self.__projects:
            if project.budget > largest_project.budget:
                largest_project = project
        return largest_project
    
    def get_active_projects(self) -> list[Project]:
        active_projects: list[Project] = []
        for project in self.__projects:
            if project.active:
                active_projects.append(project)
        return active_projects
    


def main() -> None:
    p1 = Programmer("Lily", "C++, Java", 10000)
    p2 = Programmer("Judy", "Python, Java", 18000)
    m = Manager("Peter", "Management", 20000, 20000)
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
    
    