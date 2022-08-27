#Rock Paper Scissors Game

from asyncore import loop
import random
from timeit import repeat



while True:
    a = input("Choose your move(rock, paper, or scissors): ")
    print("You chose", a)

    choice2 = ['rock', 'paper', 'scissors']
    comp = random.choice(choice2)
    print("I chose", comp)
    if a == comp:
        print("It's a tie!")
    elif a == "rock":
                comp == "scissors"
                print("You win!")
    elif a == "paper":
                comp == "scissors"
                print("I win!")

    elif a == "scissors":
                    comp == "rock"
                    print("I win!")

    elif a == "rock":
                    comp == "paper"
                    print("I win!")

    elif a == "paper":
                    comp == "rock"
                    print("You win!")

    elif a == "scissors":
                    comp == "paper"
                    print("You win")

    end = input("Do you want to go again? ")
    if end == "yes":
                repeat()
    elif end == "no":
        break