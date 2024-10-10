#Exerise 5
#Rock Paper Scissor
#create a program to play rock paper scissor
import random as r

choice  = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
game = ((0,-1,1),(1,0,-1),(-1,1,0))

def User_ip():
    user = int(input("Enter your choice(0-Rock/1-Paper/2-Scissor): "))
    while user not in choice:
        user = int(input("\r Wrong input enter your choice again(0-Rock/1-Paper/2-Scissor): "))
    return user

def Comp_ip():
    comp = r.randint(0,2)
    return comp
        
def check(user,comp):
    return game[comp][user]



def startgame():
    user = User_ip()
    comp = Comp_ip()
    print(f"Your choose {choice[user]}")
    print(f"Computer choose {choice[comp]}")
    result = check(user,comp)
    if result == -1:
        print('You loss')
    elif result == 0:
        print('Game Tie')
    else:
        print('You Won')
startgame()
