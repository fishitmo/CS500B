# print the program title 
print("Question 1: Capitalizing Each word")


# Prompt the user to enter a sentence
str_input = input("Please enter a sentence:")

# Process each character to capitalize the first letter of each word

result = ""
pre = " "
for ch in str_input:
   if pre == " " and ch != " ": 
      result +=ch.capitalize()
   else:
       result += ch
   pre = ch
   
# print the result string
print("The output is", result)    
    