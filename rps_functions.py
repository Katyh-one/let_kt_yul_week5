# Import the random module to generate random choices
from random import randint


# todo: Function returns computer and user choice
# FUNCTION CHOICES: set of instructions for player to input choice and computer to randomly choose choice
# No parameters within the parenthesis as objects are returned as local references are changed in the function
# return objects of references user_choice and computer_choice as they are altered by user and computer
def choices():
    # list with assigned items r, p, s for computer random choice and user choice
    choice_list = ["Rock", "Paper", "Scissors"]
    # Prompt the user to enter their choice
    user_choice = input("Enter your choice (Rock, Paper or Scissors): ").capitalize()

    # Generate a random choice for the computer
    computer_number = randint(0, 2)
    # slices list from the outcome of random integer to return string value from list
    computer_choice = choice_list[computer_number]
    # Print the choices made by the user and the computer
    print(f"You choose: {user_choice}\nComputer chose: {computer_choice}.")
    # Return the choices made by the user and the computer
    return user_choice, computer_choice



# # todo: determine winner

# Function to determine the winner of a single game
def determine_winner_option_one(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw!")

    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")

    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")

    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("Computer wins, better luck next time!")


# todo: create a function that allows user to play out of 3 and ends game
# Function to determine the winner in a best of three games scenario
def determine_winner_option_two(user_choice, computer_choice, computer_score, user_score):
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
        # adds 1 to the user score board
        user_score += 1
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
        user_score += 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins, better luck next time!")
        computer_score += 1
    # Return the updated scores
    return user_score, computer_score

# or statement to be able to lge
# Function to display the score board
def score_board(user_score, computer_score, number_of_rounds):
    print(f"{"~" * 30}\n Num of Rounds: {number_of_rounds + 1}")
    print(f"{"-" * 5} Score Board {"-" * 5}")
    print(f"Your Score: {user_score} | Computer: {computer_score}")
    print(f"{"~" * 30}")
    # Return the number of rounds and the scores
    return number_of_rounds, user_score, computer_score


# def final_score(user_score, computer_score):
#     if user_score == computer_score:
#         print("Draw!!")
#     elif user_score > computer_score:
#         print(f"Congrats, You won the game!!")
#     else:
#         print(f"Computer won the game!! Better luck next time!")


if __name__ == "__main__":
    choices()
    determine_winner_option_one()
    determine_winner_option_two()
    score_board()