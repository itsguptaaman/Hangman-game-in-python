# Creating a hangman game

# importing random function
import random

# Creating a function
def hangman():
    # Creating alist that stores words
    word=random.choice(["sunday","monday","tuesday","wednesday","thursday",'friday','saturday'])
    # To check letter is valid creating validLetter variable and storeing the letters
    validLetters="abcdefghijklmnopqrstuvwxyz"
    # Number of turns player will get
    turns=10
    guessMade=''
    #creating loops
    while len(word)>0:
        # main will store the main word from list
        main=""
        missed=0
        for letter in word:
            if letter in guessMade:
                main=main+letter
            else:
                main=main+"_"+""
        #if the letters are complete user will win
        if main==word:
            print(main)
            print("You Won the game!")
            break
        print("Guess the word ",main)
        guess=input()
        if guess in validLetters:
            guessMade= guessMade+guess
        else:
            print("The entered letter is not valid! ")
            guess=input()
        # if user enter the worn letter
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left !")
                print("    ______    ")
            if turns==8:
                print("8 turns left !")
                print("    _______   ")
                print("       0      ")
            if turns==7:
                print("7 turns left !")
                print("    _______   ")
                print("       0      ")
                print("       |      ")
            if turns==6:
                print("6 turns left !")
                print("    _______   ")
                print("       0      ")
                print("       |      ")
                print("      /       ")
            if turns==5:
                print("5 turns left !")
                print("    _______   ")
                print("       0      ")
                print("       |      ")
                print("      / \     ")
            if turns==4:
                print("4 turns left !")
                print("    _______   ")
                print("     \ 0      ")
                print("       |      ")
                print("      / \     ")
            if turns==3:
                print("3 turns left !")
                print("    _______   ")
                print("     \ 0 /    ")
                print("       |      ")
                print("      / \     ")
            if turns==2:
                print("2 turns left !")
                print("    _______   ")
                print("     \ 0 /|   ")
                print("       |      ")
                print("      / \     ")
            if turns==1:
                print("1 turns left !")
                print("Man is taking his last breath")
                print("    _______   ")
                print("     \ 0_|/   ")
                print("       |      ")
                print("      / \     ")
            if turns==0:
                print("You lose!")
                print("You let a kind man die")
                print("    _______   ")
                print("       0_|     ")
                print("      /|\      ")
                print("      / \     ")
                break

# Staring interface
name=input("Enter your name :")
print(f"Hello {name}! Lets start the game...")
print("________________________________________")
print("Try to guess the words under 10 attempts!")
hangman()
print()
