"""Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following:
Too high
Too low
Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly."""
import random

def guessing_game():
    selected_nr = random.randint(0,100)
    print(selected_nr)
    guess_nr = -1
    while selected_nr != guess_nr:
        guess_nr = int(input("Guess what number has been chosen:"))
        if guess_nr > selected_nr:
            print("Too high")
            continue
        elif guess_nr < selected_nr:
            print("Too low")
            continue
        elif guess_nr == selected_nr:
            break
    return "Just right"

print(guessing_game())
