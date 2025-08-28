'''
Case Study - A Warning notice based on average

- The notices program determines:
    1. a students average based on three test scores and
    
    2. the student's passing/failig status
      
'''

# display the program status
print("The notice program")
print()

# get user inputs 

student_id = int(input("Enter the student id:"))
test1 = int(input("Enter first score (0-100):"))
test2 = int(input("Enter srcond score (0-100): "))
test3 = int(input("Enter third score (0-100): "))
print()
print("Student number:", student_id)
print("Test scores:", test1, test2, test3)

# Calculate the averge of three test grades and 
# determine whether or not the student is passing 

if test1<0 or test2<0 or test3<0:
    dataok = 0
else:
    dataok = 1

if dataok:
    average = (test1 + test2 + test3)/3
    print("Average Score is:", round(average,2))
    
    if average >= 60.0:
        notice= "Passing\t"
        if average >=70:
            notice += "but marginal"
        print(notice + ".")
    else:
        print("Failing.")
else:
    print("Invalide Data: Scores less than zero.\n")
print()
print("Bye")                         
     
 