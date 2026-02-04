import random

print("Welcome to the Dice Rolling Game!")

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    

    if choice == 'n':
        print("Thanks for playing! Goodbye.")
        break   
    elif choice == 'y':
        dice_count = 0
        while dice_count <= 0:
            dice_count_input = input("How many dice would you like to roll? : ")
            if dice_count_input.isdigit():
                dice_count = int(dice_count_input)
            if dice_count <= 0:
                print("Please enter a valid positive number for the number of dice.")
        total = 0
        for i in range(dice_count):
            roll = random.randint(1, 6)
            total += roll
        print(f"You rolled {dice_count} dice and got a total of {total}.")
    else:
        print("Invalid input. Please enter 'y' to roll or 'n' to quit.")