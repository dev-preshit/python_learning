#Exerise 5
#Rock Paper Scissor
#create a program to play rock paper scissor
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
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

startgame()