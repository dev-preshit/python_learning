#EXECRISE 5
#Rock Paper Scissor
#Create a Rock Paper sicssor game in python
"""
    Explanation:

    Choices and Game Rules:
        • We define a choice dictionary where the keys are numbers representing Rock, 
        Paper, and Scissors, and the values are the corresponding names as strings.
        • The game tuple is a 2D matrix where each element represents the result of a match between 
        two choices. The rows represent the computer's choice and the columns represent the user's choice. 
        For example:
            (0, -1, 1) means that if the computer chooses Rock (index 0), the result will be:
                • 0 (tie) if the user also chooses Rock,
                • -1 (loss for the user) if the user chooses Scissors,
                • 1 (win for the user) if the user chooses Paper.

    Functions:

        • User_ip(): This function takes the user's choice as input and ensures it's valid (only 0, 1, or 2). 
        If the input is invalid, it asks for input again.
        • Comp_ip(): This function generates a random choice for the computer using 
        random.randint(), which picks a number between 0 and 2.
        • check(user, comp): This function compares the user’s choice and the computer’s choice using the game tuple. 
        It returns 0 for a tie, -1 for a loss, and 1 for a win.
        • startgame(): This function controls the game. It gets the user's and computer's choices, 
        prints them, and displays the result based on the return value of check().
"""
import random as r

choice = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
game = ((0, -1, 1), (1, 0, -1), (-1, 1, 0))

def User_ip():
    while True:
        try:
            user = int(input("Enter your choice (0-Rock / 1-Paper / 2-Scissor): "))
            if user in choice:
                return user
            else:
                print("Invalid choice. Please choose 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

def Comp_ip():
    return r.randint(0, 2)
        
def check(user, comp):
    return game[comp][user]

def startgame():
    rounds = 0
    user_score = 0
    comp_score = 0
    ties = 0

    while True:
        user = User_ip()
        comp = Comp_ip()
        print(f"You chose: {choice[user]}")
        print(f"Computer chose: {choice[comp]}")

        result = check(user, comp)
        if result == -1:
            print('You lost this round.')
            comp_score += 1
        elif result == 0:
            print('This round is a tie.')
            ties += 1
        else:
            print('You won this round!')
            user_score += 1
        
        rounds += 1
        print(f"\nScore after {rounds} round(s):")
        print(f"You: {user_score}, Computer: {comp_score}, Ties: {ties}\n")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

startgame()

