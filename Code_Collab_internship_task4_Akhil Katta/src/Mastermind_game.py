import random

def validate_input(prompt, length):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and len(user_input) == length:
            return user_input
        print(f"Invalid input! Please enter a {length}-digit number.")

def compare_numbers(secret, guess):
    correct_digits = 0
    correct_positions = 0

    for s_digit, g_digit in zip(secret, guess):
        if g_digit in secret:
            correct_digits += 1
        if s_digit == g_digit:
            correct_positions += 1
    
    return correct_digits, correct_positions

def guessing_round(player_num, secret, length):
    attempts = 0
    while True:
        guess = validate_input(f"Player {player_num}, enter your {length}-digit guess: ", length)
        attempts += 1
        correct_digits, correct_positions = compare_numbers(secret, guess)
        print(f"Player {player_num}'s guess: {guess} | Correct digits: {correct_digits}, Correct positions: {correct_positions}")

        if correct_positions == length:
            print(f"Player {player_num} guessed the number in {attempts} attempts!")
            return attempts

def mastermind_game():
    print("Welcome to Mastermind Game!")

    length = int(input("Enter the length of the secret number: "))

    print("Player 1, set your secret number.")
    secret_player1 = validate_input(f"Enter a {length}-digit secret number for Player 2 to guess: ", length)

    print("\n" * 50)

    attempts_player2 = guessing_round(2, secret_player1, length)

    print("Player 2, set your secret number.")
    secret_player2 = validate_input(f"Enter a {length}-digit secret number for Player 1 to guess: ", length)

    print("\n" * 50)

    attempts_player1 = guessing_round(1, secret_player2, length)

    print("\nFinal Results:")
    print(f"Player 1 took {attempts_player1} attempts.")
    print(f"Player 2 took {attempts_player2} attempts.")

    if attempts_player1 < attempts_player2:
        print("Player 1 wins!")
    elif attempts_player2 < attempts_player1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    mastermind_game()
