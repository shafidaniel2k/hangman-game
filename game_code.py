import time
import random
question = input("Start a new game, yes or no?\n").lower()
if question == "no":
    print("That's a shame.")
while question == "yes":
    name = input("What's your name? \n")
    while name == "":
        name
    else:
        break
if question == "yes":
    print("""
-----------------------------------
|Welcome to leinad's hangman game!|
-----------------------------------
""")
while question == "yes":
    time.sleep(1)
    print("The game has started.")
    secret_word = random.choice(["gucci", "flight", "swiss"])
    guesses = ""
    turns = 10
    points = 0
    if points > 0:
        print(f"You have {points} victory points!")
    while turns > 0:
        counter = 0
        for char in secret_word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_ ", end=" ")
                counter += 1
        if counter == 0:
            print("Victory!")
            points += 1
            questionVic = input("Start a new game, yes or no?\n").lower()
            if questionVic == "yes":
                break
            else:
              "Thanks for playing."
        guess = input("\nGuess a character: ")
        guesses += guess
        if guess not in secret_word:
            turns -= 1
            print("Incorrect, you have " + str(turns) + " turns left.")
        else:
            print("Correct.")
        if turns == 0:
            print("You lost.")
            points = 0
            questionLos = input("Start a new game, yes or no?\n").lower()
            if questionLos == "yes":
                break
            else:
              "Thanks for playing."
