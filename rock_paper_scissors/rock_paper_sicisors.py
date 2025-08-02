import random

def print_intro():
    print("Rock, Paper, Scissors game by B.P.X")
    print("-" * 30)

hands = ['r', 'p', 's']
hand_dict = {
    "r": "🪨",
    "p": "📃",
    "s": "✂️"
}
best_score = None

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in hands:
            return user_input
        else:
            print("Invalid choice!\nPlease enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")

def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes/no)\n> ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            print("Thanks for playing! 👋")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def check_win(user_choice, cpu_choice):
    win_conditions = {
        'r': 's',  # Rock beats Scissors
        'p': 'r',  # Paper beats Rock
        's': 'p'   # Scissors beats Paper
    }
    if user_choice == cpu_choice:
        print("It's a Draw!")
        return "draw"
    elif win_conditions[user_choice] == cpu_choice:
        print("You Win!")
        return "win"
    else:
        print("You Lose!")
        return "lose"

def game():
    global best_score
    current_wins = 0
    print_intro()
    while True:
        cpu_hand = random.choice(hands)
        usr_hand = get_user_input("Rock, Paper or Scissors? (r/p/s): ")
        print(f"You Choose: {hand_dict.get(usr_hand)}")
        print(f"Computer Choose: {hand_dict.get(cpu_hand)}")
        result = check_win(usr_hand, cpu_hand)
        if result == "win":
            current_wins += 1
            if best_score is None or current_wins > best_score:
                best_score = current_wins
                print(f"{current_wins} win(s).\nThis is your best score so far!")
            else:
                print(f"Your best score remains {best_score}.")
        if not play_again():
            break

game()