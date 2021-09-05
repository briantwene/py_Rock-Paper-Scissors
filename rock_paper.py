#File: rock_paper.py
#Author: Brian Twene(@bt521)
#Date: 04/09/2021

#import the random library
import random

#dictionary that represents the players choices
weapon = {"r":"rock","p":"paper","s":"scissors"}

#function for getting user input
def getUserInput():
    #ask for user input
    playerChoice = input("select your weapon: R - Rock, P - Paper, S - Scissors: ")

    #keep looping until user enters an action that is in the dictionary
    while playerChoice not in weapon:
        #display error and ask user to enter again
        print("invalid choice!")
        playerChoice = input("select your weapon: R - Rock, P - Paper, S - Scissors")
    #return the action once finished
    return playerChoice


#function for generating opponent actions
def randomChoice():
    #pick a random action from the dictionary
    cpuChoice = random.choice(list(weapon))
    #return it to the calling function
    return cpuChoice


def determineWinner(playerChoice, cpuChoice):

    #display the opponents action
    print("CPU chose",weapon[cpuChoice])

    #determin the winner depening on what the player chose
    if playerChoice == cpuChoice:
        print("it's a drawr")
    elif playerChoice == "r":
        if cpuChoice == "s":
            print("Rock destroys scissors, you win")
        elif cpuChoice == "p":
            print("Paper covers rock, you lose")
    elif playerChoice == "s":
        if cpuChoice == "p":
            print("scissors shreds paper, you lose")
        elif cpuChoice == "r":
            print("Rock destroys scissors, you lose")
    elif playerChoice == "p":
            if cpuChoice == "r":
                print("Paper covers rock, you win")
            elif cpuChoice == "s":
                print("scissors shreds paper, you lose")


#main function for running it all
def main():
    playerChoice = getUserInput()
    cpuChoice = randomChoice()
    determineWinner(playerChoice,cpuChoice)


main()
