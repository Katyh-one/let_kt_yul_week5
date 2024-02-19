import random

def get_user_choice():
    """
    Get the user to enter their choice (R, P, or S).
    """
    user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
    while user_input not in ['R', 'P', 'S']:
        print("Invalid choice. Please enter R, P, or S.")
        user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
    return user_input

def convert_choice(choice):
    """
    Convert the user's choice into the full word (Rock, Paper, or Scissors).
    """
    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissors'

def get_computer_choice():
    """
    Generate a random choice for the computer.
    """
    return random.choice(['R', 'P', 'S'])

def determine_winner(user_choice, computer_choice):
    """
    Compare the choices and determine the winner.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'P' and computer_choice == 'R') or \
         (user_choice == 'S' and computer_choice == 'P'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """
    Main function to run the game.
    """
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    user_choice_full = convert_choice(user_choice)
    computer_choice = get_computer_choice()
    computer_choice_full = convert_choice(computer_choice)
    print("You chose:", user_choice_full)
    print("Computer chose:", computer_choice_full)
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
