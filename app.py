#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
#print("Hello world!")

"""Develop a game of rock paper scissors multiplayer, where scissors beats paper, paper beats rock, and rock beats scissors
the first to 3 wins is the winner
the game will be played in the console
the computer will make a random choice each time, and the player will be prompted for their choice
the player will enter their choice using the keyboard
the program will display the result of each round
the program will display the final score and the winner"""

"""Welcome to Rock, Paper, Scissors!
You will be playing against the computer, and the first to 3 wins is the winner!
The rules are simple, scissors beats paper, paper beats rock, and rock beats scissors.
Good luck!"""

"""Enter your move: (r)ock (p)aper (s)cissors or (q)uit
r
ROCK versus...
PAPER
You lose!
0 Wins, 1 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
r
ROCK versus...
SCISSORS
You win!
1 Wins, 1 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
r
ROCK versus...
ROCK
It's a tie!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
Thanks for playing!"""
import random
import sys

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer, and the first to 3 wins is the winner!")
print("The rules are simple, scissors beats paper, paper beats rock, and rock beats scissors.")
print("Good luck!")

wins = 0
losses = 0
ties = 0

while True: #the main game loop
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True: #the player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit() #quit the program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break #break out of the player input loop
        print("Type one of r, p, s, or q.")
    #display what the player chose:
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")
    #display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")
    #display and record the win/loss/tie
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
