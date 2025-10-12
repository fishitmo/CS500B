class CourseFile:
    def __init__(self, filename: str) -> None:
        self.__filename = filename
        
    def writeCourses(self, courses):
        with open(self.__filename, "w") as file:
            for course in courses:
                file.write(course + "\n")
    

def main():
    file = CourseFile("courses.txt")