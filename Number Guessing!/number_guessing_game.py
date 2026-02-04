import random

number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
guess = 0

while guess != number:
    # Important things to note: 
    # input() returns a string, so we need to convert it to an integer
    # isinstance checks to ensure the input is of type int
    try:
        guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")     
        continue
    if not isinstance(guess, int):
        print("Please enter a valid number.")
        continue
    if guess <= 0:
        print("Please enter a positive number.")
        continue
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")