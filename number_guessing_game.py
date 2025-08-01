from random import randint

best_score = None

def print_intro():
    print("Number Guessing Game, by B.P.X")
    print("-" * 30)

def secret_num(a,b):
    secret_number = randint(a,b)
    return secret_number

def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no)\n> ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            print("Thanks for playing! 👋")
            return False
        else:
            print("❌ Please enter 'yes' or 'no'.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

def check_number(max_guess_count, correct_answer, c, d):
    global best_score
    guess_count = 1
    while guess_count <= max_guess_count:
        user_guess = get_positive_int(f"Try {guess_count}, Guess the number (between {c} and {d}): ")
        if user_guess == correct_answer:
            print(f"\n🎉 Congratulations! You guessed the number in {guess_count} attempt(s) 🎉")
            if best_score is None or guess_count < best_score:
                best_score = guess_count
                print("🥇 This is your best score so far!")
            else:
                print(f"⭐ Your best score remains {best_score} attempt(s).")
            break
        elif user_guess < correct_answer:
            print(f"Think Higher")
        elif user_guess > correct_answer:
            print(f"Think Lower")
        guess_count += 1
    else:
        print(f"Game Over! You've used all {max_guess_count} tries.")
        print(f"The correct number was: {correct_answer}")

def number_guessing_game():
    global best_score
    print_intro()
    while True:
        starting_range = get_positive_int(f"Enter a Starting range number (Greater than 0): ")
        last_range = get_positive_int(f"Enter a Last range number: ")
        if starting_range >= last_range:
            print("Starting range must be less than ending range. Try again.")
            continue
        guess_count = get_positive_int(f"How many tries(Greater than 0): ")
        answer = secret_num(starting_range, last_range)
        check_number(guess_count, answer, starting_range, last_range)
        if not play_again():
            break

number_guessing_game()
