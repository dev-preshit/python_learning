#EXECRISE 5
#Rock Paper Scissor
#Create a Rock Paper sicssor game in python
"""
    We created a function that will take user input 0-Rock/1-Paper/2-Scissor and that use that input as index
    for a tuple name game = ((0,-1,1),(1,0,-1),(-1,1,0)) which is created as the game will be draw of player will win
    or will loss, -1 for loss 0 for tie and 1 for win..
    An another function called Comp_ip there random number is generated between 0 and 1 as of index for tuple game,
    this both input are taken in check function where it return the element of that perticular index which could be -1, 0 or 1
    representing loss, tie or win.
    Than in function startgame we display the choicers of player and computer and the result...
"""
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
