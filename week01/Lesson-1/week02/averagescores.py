#!/usr/bin/env python3

# display the program title
print("The Test Scores program")
print()

print("Enter 911 to end input")

# initialize variables
num_scores = 0
total_score = 0
test_score = 0

while True:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <= 100:
        total_score += test_score
        num_scores += 1
    elif test_score == 911:
        break
    else:
        print("Test score must be from 0 through 100."
              + "Score discarded. Try again.")

# calculate average score
if num_scores > 0:
	average_score = round(total_score / num_scores, 2)
else:
	average_score = 0.0
                
# format and display the result
print("======================")
print("Total Score:", total_score, "\nAverage Score:", average_score)
print()
print("Bye")


