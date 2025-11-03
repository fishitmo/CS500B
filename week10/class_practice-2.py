from __future__ import annotations

from abc import ABC,abstractmethod

import enum


class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o):
        pass
    
    @abstractmethod
    def removeobserver(self, o):
        pass
    
    @abstractmethod
    def notifyObserver(self):
        pass
    
    
class Obsever(ABC):
    @abstractmethod
    def update(self, data):
        pass
    
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass
    
class CourseData(Subject, Displayable):
      def __init__(self):
         self.__observers = []
         self.__averageAttendance = 0.0
         self.__averageScore = 0.0
         
         
      def registerObserver(self, o):
          self.__observers.append(o)
          
          
      def removeobserver(self, o):
          i = self.__observers.index(o)
          if i >=0:
              self.__observers.pop(i)
              
      @property
      def averageAttendance(self):
          return self.__averageAttendance
      
      
      @property
      def averageScore(self):
          return self.__averageScore
      
      @averageAttendance.setter
      def averageAttendance(self, value):
          if self.__averageAttendance != value:
              self.__averageAttendance = value
              self.notifyObserver() 
              
      @averageScore.setter
      def averageScore(self, value):
         if self.__averageScore != value:
             self.__averageScore = value
             self.notifyObserver()
             
      def notifyObserver(self):
         for o in self.__observers:
             o.update()
             print()
             
      def display(self):
          print("Average Attendance =", self.__averageAttendance)
          print("Average Score =", self.__averageScore)

class Professor(Obsever, Displayable):
    def __init__(self, name):
        self.__name =  name
        
        
    def display(self):
        print("name =", self.__name)
        
    def update(self):
        print(self.__name, "got the voice")
        self.display()
        print()
        
def main():
    
    cd = CourseData()
    prof1 = Professor("Henry")
    cd.registerObserver(prof1)
    
    prof2 = Professor("Jack")
    cd.registerObserver(prof2)
    
    cd.averageAttendance = 75.5

if __name__ =="__main__":
    main()