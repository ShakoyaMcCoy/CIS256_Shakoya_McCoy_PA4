# Shakoya McCoy
# CIS256 Fall 2026
# Programming Assignment 4

import random

# Picks a random car brand from the list.
car_brands = ["Toyota", "Lexus", "Honda", "Mazda", "Tesla", "Nissan"]
chosen_brand = random.choice(car_brands)

# Tile and instructions to the game.

print("                 Reveal the Car Brand                       ")
print("Guess one letter at a time. You have 15 attempts. Good luck!")

# Creates the amount of attempts the users has.
attempts = 15

letters_guessed = [] 

# Allow the user to keep guessing letters as it displays how many attempts are left.
while attempts > 0:
    guess = input("Guess a letter:").lower()

    # Check to see if letter matches car brand listed.
    if guess in chosen_brand.lower():
        letters_guessed.append(guess)
        print ("Yay! Keep guessing!")
        
    # Minus attempts if letter is incorrect.
    else:
        attempts -= 1
        print("That is incorrect!")
        print(f"Attempts remaining: {attempts}")

    word_progress = ""
    word_complete = True

    # Check each letter in the car brand.
    for letter in chosen_brand.lower():

        # Show the letter if guessed correctly.
        if letter in letters_guessed:
            word_progress = word_progress + letter + " "

        # Leave space blank if the letter wasn't guessed correctly.
        else:
            word_progress = word_progress + "_"
            word_complete = False
            
    # Show progress after each guess.
    print(word_progress)

    # End the game and let user know they have completed it.
    if word_complete:
        print("You did an awesome job and guessed it correctly.")
        break
    
# Notify user attempts have ran out.
if attempts == 0:
    print("Better luck next time!")
