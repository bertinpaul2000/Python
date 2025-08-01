# print("""I am thinking of a 3-digit number. Try to guess what it is.
# Here are some clues:
# When I say:     That means:
# Pico            One digit is correct but in the wrong position.
# Fermi           One digit is correct and in the right position.
# Bagels          No digit is correct.""")
#
# def check_digit(user_input, secret_number):
#     if user_input == secret_number:
#         print('You got it!')
#         return
#     clues = []
#     for i in range(len(user_input)):
#         if user_input[i] == secret_number[i]:
#             clues.append("Fermi")
#         elif user_input[i] in secret_number:
#             clues.append("Pico")
#     if not clues:
#         clues.append("Bagels")
#     clues.sort()
#     print(" ".join(clues))
#
#
# import random
#
# max_guesses = 10
# to_play = True
#
# while to_play:
#     secret_number = ''.join(random.sample("0123456789", 3))
#     print('I have thought up a number.')
#     print(f'You have {max_guesses} guesses to get it.')
#     guess_count = 0
#     while guess_count < max_guesses:
#         guess_count += 1
#         print(f"Guess #{guess_count}:")
#         user_answer = input("> ")
#         if not user_answer.isdigit() or len(user_answer) != 3:
#             print("Invalid input. Enter a 3 digit Number Only.")
#             continue
#         check_digit(user_answer, secret_number)
#         if user_answer == secret_number:
#             break # They're correct, so break out of this loop.
#         if guess_count == max_guesses:
#             print('You ran out of guesses.')
#             print(f'The answer was {secret_number}.')
#     # continue game
#     print("Do you want to play again? (yes or no)")
#     to_continue = (input("> ")).lower()
#     if to_continue == "no":
#         to_play = False


# print("""I am thinking of a 3-digit number. Try to guess what it is.
# Here are some clues:
# When I say:     That means:
# Pico            One digit is correct but in the wrong position.
# Fermi           One digit is correct and in the right position.
# Bagels          No digit is correct.""")
#
# def check_digit(user_input, secret_number):
#     if user_input == secret_number:
#         print('You got it!')
#         return
#     clues = []
#     for i in range(len(user_input)):
#         if user_input[i] == secret_number[i]:
#             clues.append("Fermi")
#         elif user_input[i] in secret_number:
#             clues.append("Pico")
#     if not clues:
#         clues.append("Bagels")
#     clues.sort()
#     print(" ".join(clues))
#
#
# import random
#
# max_guesses = 10
# to_play = True
#
# while to_play:
#     secret_number = ''.join(random.sample("0123456789", 3))
#     print('I have thought up a number.')
#     print(f'You have {max_guesses} guesses to get it.')
#     guess_count = 0
#     while guess_count < max_guesses:
#         guess_count += 1
#         print(f"Guess #{guess_count}:")
#         user_answer = input("> ")
#         if not user_answer.isdigit() or len(user_answer) != 3:
#             print("Invalid input. Enter a 3 digit Number Only.")
#             continue
#         check_digit(user_answer, secret_number)
#         if user_answer == secret_number:
#             break # They're correct, so break out of this loop.
#         if guess_count == max_guesses:
#             print('You ran out of guesses.')
#             print(f'The answer was {secret_number}.')
#     # continue game
#     print("Do you want to play again? (yes or no)")
#     to_continue = (input("> ")).lower()
#     if to_continue not in ["yes", "y"]:
#         to_play = False

def print_intro():
    print("""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.""")

import random

def check_digit(user_input, secret_numbers):
    if user_input == secret_numbers:
        print('You got it!')
        return True
    clues = []
    for i in range(len(user_input)):
        if user_input[i] == secret_numbers[i]:
            clues.append("Fermi")
        elif user_input[i] in secret_numbers:
            clues.append("Pico")
    if not clues:
        clues.append("Bagels")
    clues.sort()
    print(" ".join(clues))
    return False

def play_game():
    max_guess = 10
    secret_number = ''.join(random.sample("0123456789", 3))
    print('I have thought up a number.')
    print(f'You have {max_guess} guesses to get it.')

    guess_counts = 0
    while guess_counts < max_guess:
        guess_counts += 1
        print(f"Guess #{guess_counts}:")
        user_answer = input("> ")
        if not user_answer.isdigit() or len(user_answer) != 3:
            print("Invalid input. Enter a 3 digit Number Only.")
            guess_counts -= 1 # Do not count invalid inputs
            continue
        if check_digit(user_answer, secret_number):
            return # Win and exit game
    print('You ran out of guesses.')
    print(f'The answer was {secret_number}.')



def main_game():
    print_intro()
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes or no)\n> ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing Bagels. Goodbye!")
            break
main_game()