import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return (dice1, dice2)


def main():
    continue_game = True
    while continue_game:
        print("Roll the dice? (y/n)")
        answer = input()
        if answer == 'y':
            dice1, dice2 = roll_dice()
            print(f"Dice 1: {dice1}, Dice 2: {dice2}")
        elif answer == 'n':
            continue_game = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    print("Goodbye!")
    
if __name__ == "__main__":
    main()