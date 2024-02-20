import random


# get_user_choice() gets the user to input their choice of 'R', 'P', or 'S' for Rock, Paper, or
# Scissors respectively, using a while loop to ensure that the user enters a valid choice and
# prompts them again if the input is not one of the specified options.The function returns the
# validated user input in uppercase.
def get_user_choice():
    """
    Get the user to enter their choice (R, P, or S).
    """
    user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
    while user_input not in ['R', 'P', 'S']:
        print("Invalid choice. Please enter R, P, or S.")
        user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
    return user_input


# convert_choice() takes a single argument choice, which represents the user's input ('R', 'P', or 'S').
# It converts the abbreviated user choice into the full word ('Rock', 'Paper', or 'Scissors') and
# returns it.
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


# This function get_computer_choice() randomly selects one of 'R', 'P', or 'S' for the computer's choice
# (Rock, Paper, or Scissors) using random.choice() from the random module.
def get_computer_choice():
    """
    Generate a random choice for the computer.
    """
    return random.choice(['R', 'P', 'S'])

# determine_winner() compares the user's choice with the computer's choice and determines the winner
# based on the rules of Rock, Paper, Scissors.
# It returns a string indicating the outcome: either a tie, the user wins, or the computer wins.
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

# main() is the entry point of the program.
# Prints the introductory message, calls get_user_choice() to get the
# user's input, and convert_choice() to convert it into the full word.
# It then calls get_computer_choice() to get the
# computer's random choice and converts it similarly.
# Finally, it prints both choices and the outcome determined by
# determine_winner().
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

# is a Python idiom that checks whether the script is being run directly by the interpreter
# or if it is being imported as a module into another script.
if __name__ == "__main__":
    main()
