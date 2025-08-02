import random

def roll_dice(no):
    output = ()
    for item in range(no):
        num = random.randint(1, 6)
        output += (num,)
    return output

counter = 1

while True:
    print(f"Roll Count = {counter}")
    user_input = input("Roll the Dice? (Y/N)\n> ").strip().upper()
    if user_input == "N":
        print("Thankyou for playing.\nGoodbye!")
        break
    elif user_input == "Y":
        while True:
            try:
                no_of_dice = int(input("How many dice you want to roll?\n> ").strip())
                if no_of_dice <= 0:
                    count = counter + 1
                    print("Please enter a number greater than 0.")
                    continue
                result = roll_dice(no_of_dice)
                print(f"You Rolled: {result}\n ____________________")
                counter += 1
                break
            except ValueError:
                print("Invalid number! Please enter a valid integer.")
    else:
        print("""Please enter "Y" or "N""")