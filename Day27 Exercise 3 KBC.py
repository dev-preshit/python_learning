#EXECRISE 3
#Kaun Banega Crorepati (KBC)
#create a KBC game which have question and keep track of winning amount

import random

playerName = input("Enter your name: ")
print(f"Wecome {playerName} to KBC:")

Question = ["Which of the following is the correct syntax to print \"Hello, World!\" in Python?",
            "Which of the following data types is immutable in Python?",
            "What is the correct file extension for Python files?",
            "How do you insert comments in Python?",
            "Which keyword is used to define a function in Python?"]

Option = [("A) echo \"Hello, World!\"","B) printf(\"Hello, World!\")","C) print(\"Hello, World!\")","D) print(\"Hello\", \"World!\")"),
          ("A) List","B) Dictionary","C) Set","D) Tuple"),
          ("A) .pyth","B) .py","C) .pt","D) .python"),
          ("A)// This is a comment","B) /* This is a comment */","C) # This is a comment","D) <!-- This is a comment -->"),
          ("A) def","B) func","C) define","D) function")]

Answer = ("C) print(\"Hello, World!\")","D) Tuple","B) .py","C) # This is a comment","A) def")

price = (0,10000,20000,50000,100000,500000)


list = []
while len(list) < 5:
    random_number = random.randint(0, len(Question)-1)
    if random_number not in list:
        list.append(random_number)


QueNo = 0
for i in list:
    input()
    print(Question[i])

    for j in range(4):
        print(Option[i][j])

    Ans = input("Enter Correct answer alphabet (A/B/C/D)\n=> ").upper()
    while Ans not in ['A', 'B', 'C', 'D']:
        print("\nInvalid input! Please enter A, B, C, or D.")
        Ans = input("Enter Correct answer alphabet (A/B/C/D)\n=> ").upper()

    if(Ans == Answer[i][0]):
        print(f"CORRECT ANSWER {playerName}")
        QueNo = QueNo + 1
        continue
    else:
        print(f"WRONG ANSWER {playerName}")
        break


print("\n")
if QueNo != 0:
    print(f"Congo {playerName} you Won {price[QueNo]}")
else:
    print(f"Sorry {playerName} you Won {price[QueNo]}")