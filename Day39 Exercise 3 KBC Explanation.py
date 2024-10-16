# EXERCISE 3
# Kaun Banega Crorepati (KBC) Explanation
# Create a KBC game which has questions and keeps track of the winning amount.

"""
    My logic was to create a question list, an option list, an answer list, and a price list.
    The index of questions with their options and answers are the same, so that if we call an 
    index for all lists, it will fetch the correct list element...

    This index generation is set to random by using the random module.
    Then, I create an empty list and append random numbers into it in the range from 0 to 
    the length of the list - 1, which will call each element of the list using a for loop 
    that works as an index for all parameter lists...

    Then take the valid input from the user, convert it to uppercase, check if the answer 
    list and the user input match. If yes, then print the correct answer and display the 
    next question. If wrong, break the loop and display the winning amount...
"""

import random

playerName = input("Enter your name: ")
print(f"Welcome {playerName} to KBC:")

Questions = [
    "Which of the following is the correct syntax to print \"Hello, World!\" in Python?",
    "Which of the following data types is immutable in Python?",
    "What is the correct file extension for Python files?",
    "How do you insert comments in Python?",
    "Which keyword is used to define a function in Python?"
]

Options = [
    ("A) echo \"Hello, World!\"", "B) printf(\"Hello, World!\")", "C) print(\"Hello, World!\")", "D) print(\"Hello\", \"World!\")"),
    ("A) List", "B) Dictionary", "C) Set", "D) Tuple"),
    ("A) .pyth", "B) .py", "C) .pt", "D) .python"),
    ("A) // This is a comment", "B) /* This is a comment */", "C) # This is a comment", "D) <!-- This is a comment -->"),
    ("A) def", "B) func", "C) define", "D) function")
]

Answers = ("C) print(\"Hello, World!\")", "D) Tuple", "B) .py", "C) # This is a comment", "A) def")

prices = (0, 10000, 20000, 50000, 100000, 500000)

# Create a list of random questions
question_indices = []
while len(question_indices) < 5:
    random_number = random.randint(0, len(Questions) - 1)
    if random_number not in question_indices:
        question_indices.append(random_number)

QueNo = 0
for i in question_indices:
    input("Press Enter to continue...")
    print(Questions[i])

    for j in range(4):
        print(Options[i][j])

    Ans = input("Enter the correct answer alphabet (A/B/C/D)\n=> ").upper()
    while Ans not in ['A', 'B', 'C', 'D']:
        print("\nInvalid input! Please enter A, B, C, or D.")
        Ans = input("Enter the correct answer alphabet (A/B/C/D)\n=> ").upper()

    if Ans == Answers[i]:
        print(f"CORRECT ANSWER {playerName}!")
        QueNo += 1
    else:
        print(f"WRONG ANSWER {playerName}.")
        break

print("\n")
if QueNo != 0:
    print(f"Congratulations {playerName}, you won {prices[QueNo]}!")
else:
    print(f"Sorry {playerName}, you won {prices[QueNo]}.")
