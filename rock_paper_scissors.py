import random

choices = ["rock", "paper", "scissors"]

# Player stats
user_score = 0
computer_score = 0
user_history = []
user_streak = 0
power_shield = False
double_points = False


def get_computer_choice():
    if len(user_history) == 0:
        return random.choice(choices)

    most_common = max(set(user_history), key=user_history.count)
    counter_moves = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    # Mix prediction with randomness
    if random.random() < 0.5:
        return counter_moves[most_common]
    else:
        return random.choice(choices)


def decide_winner(user_move, comp_move):
    if user_move == comp_move:
        return "draw"

    if (
        (user_move == "rock" and comp_move == "scissors") or
        (user_move == "paper" and comp_move == "rock") or
        (user_move == "scissors" and comp_move == "paper")
    ):
        return "user"

    return "computer"


def play_round():
    global user_score, computer_score, user_streak, power_shield, double_points

    user_move = input("Enter rock, paper, or scissors: ").lower()

    if user_move not in choices:
        print("Invalid choice!")
        return

    comp_move = get_computer_choice()
    user_history.append(user_move)

    print("Computer chose:", comp_move)

    result = decide_winner(user_move, comp_move)

    # Apply shield
    if power_shield and result == "computer":
        print("🛡 Shield protected you! It's a draw.")
        result = "draw"
        power_shield = False

    if result == "user":
        print("You win this round!")
        points = 2 if double_points else 1
        user_score += points
        user_streak += 1
        double_points = False

    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
        user_streak = 0

    else:
        print("It's a draw!")
        user_streak = 0

    # Unlock power-ups
    if user_streak == 3:
        print("Streak Bonus! Shield unlocked!")
        power_shield = True

    elif user_streak == 5:
        print("Mega Streak! Double Points unlocked!")
        double_points = True

    print("Score -> You:", user_score, "| Computer:", computer_score)
    print("-" * 40)


def start_game():
    print("Welcome to the Rock, Paper and Scissors Game!!")

    rounds = int(input("Enter number of rounds: "))

    for i in range(rounds):
        print("Round", i + 1)
        play_round()

    print("\nFinal Score -> You:", user_score, "| Computer:", computer_score)

    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("Computer is the overall winner!")
    else:
        print("It's a tie!")


# Run game
start_game()
