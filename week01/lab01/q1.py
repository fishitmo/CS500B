
'''
Question 1:
Write a Python program that asks for a string as input and prints a version with each word capitalized and a full stop
added at the end (if not already present). Constriants: Use character-by-character processing and string concatenation, avoiding slicing 
and string methods like upper(), title() and endswith().

'''

# print the program title 
print("Question 1: Capitalizing Each word")


# Prompt the user to enter a sentence
str_input = input("Please enter a sentence:")

# Process each character to capitalize the first letter of each word

result = ""
pre = " "
for i, ch in enumerate(str_input):
   if pre == " " and ch != " ": 
      result +=ch.capitalize()
   else:
       result += ch
   pre = ch
   
   if i == len(str_input)-1 and ch != ".":
       result += "."
   
# print the result string
print("The output is", result)    
    