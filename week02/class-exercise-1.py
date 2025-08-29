# write a ptthonn code to do a`do while loop` in C

print("Enter rainfall amount")

while True:
    amount = float(input)
    if amount < 0:
        print("Error")
    else:
        sum += amount
        break
    
# 1st approach 
def add(x,y):
    sum = x + y
    return sum

# 2nd approach 




'''
Terms 
      1. Parameters -> variables that receive arguments
      2. arguments -> values that are passed to a function


'''

def add(x,y): # x and y are parameters
    return x + y

def main():
    a = 10
    b = 20
    c = add(a,b) # a and b are arguments
    
# let's say I have a file called myprog.py


def add(x,y):
    return x + y

def main():
    sum = add(10,20)
    sum = sum + 40
    
# The main() will only be called when myprog.py is executes as a main module
if __name__ == "__main__":
    main()
    
# Local and Global Variables

