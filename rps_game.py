import rps_functions

# TODO: Game Name starts
# print function used to display the name of the gam and used upper method to make all string capital
print("rock, paper, scissors game".upper())

# # # #  TODO: to prompt the user can use an input function
# variables assigned to value 0 for function to increment the score by adding 1
computer_score = 0
user_score = 0
# variables assigned to string value numbers which is used in the while loop
play_one_game = '1'
play_three_times = '2'
# score board to show user the number of rounds
number_of_rounds = 0


# while True loop is used to execute a block of code repeatedly until boolean condition evaluated False or break
# while True means the loop will run forever or if, elif or else statement is met
while True:
    # prompts user whether or not ready to play
    game_start = input("Welcome, are you Ready to play rock, paper, scissors (yes/no)? ")
    # if statement: if user response is equal (==) string value yes
    if game_start.lower() == "yes":
        # print function used to display string message to indicate the game is starting
        print("Ok, let's go!")
        # prompts user to choose option of play game. if chooses any other option returns to beginning
        option_play = input(f"[Press 1] Play 1 game OR [Press 2] play best of 3: ")

        # if condition: user chooses to play one game. the following code executes
        if option_play == play_one_game:
            # call functions for computer choice, user_choice and to determine the winner
            # used variable user_choice, computer_choice to store the outcomes of the function
            user_choice, computer_choice = rps_functions.choices()
            # the determine_winner_option_one function uses the two parameters to find the winner and prints result
            rps_functions.determine_winner_option_one(user_choice, computer_choice)
            # break used to leave the loop and exit the game
            break
        elif option_play == play_three_times:
            for rounds in range(3):
                user_choice, computer_choice = rps_functions.choices()
                rps_functions.determine_winner_option_two(user_choice, computer_choice, user_score, computer_score)
                user_score, computer_score, number_of_rounds = rps_functions.score_board(user_score, computer_score, number_of_rounds)
            break
    elif game_start.lower() == "no":
        print('Not ready to play? Okay, see ya later!')
        break
    else:
        print("Type yes or no")
