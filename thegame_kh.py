import random
import gamefunctions_kh
# rock paper scissors - aim of the game is to get the inputs from the computer and user
# compare their inputs
# with each compare check if the user has won lost or drew against the computer
# player_wins/ computer_wins are added to each time one side wins
# the game will run until either computer or player gets to 3 wins
player_wins = 0
computer_wins = 0
# TODO: Creating a file that can then be written to with the ending match report
match_report = open('matchreport.txt', 'w')
print(f"Are you ready to play? Your choices are R, P, S. First to three wins!")
while player_wins < 3 and computer_wins < 3:
    # TODO: Prompts the user to enter a value: R,P,S
    # TODO: validate the user input to make sure it is R,S,P
    # assign the returned value to variable to be used further down
    # function is taking the input and validating that it is one of the expected values from the list
    player_input = gamefunctions_kh.validate_user()
    # TODO: The program should convert this to rock paper scissors
    # converts the players response into Rock, Paper, Scissors string to be used as comparison later
    player_choice = gamefunctions_kh.player_convert(player_input)
    print(f"Player one you have chosen {player_choice}")
    # TODO: Computer generates a random number from the list of numbers provided
    computer_outcomes = [0, 1, 2]
    # computer generates a random number from the computer_outcomes list
    computer = str(random.choice(computer_outcomes))
    # created function converts the computers choice into Rock, Paper, Scissors string to be used as comparison later
    computer_choice = gamefunctions_kh.computer_convert(computer)
    print(f"Computer you have chosen {computer_choice}")
    # TODO: Compare users choice with computers choice indicating who won
    # using the outcome to of the comparison to add to the players total
    player_win, computer_win = gamefunctions_kh.compare_outcomes(player_choice, computer_choice)
    if player_win == 'Winner':
        player_wins += 1
        print(f'You have won {player_wins} matches!')
        print('#' * 50)

    elif computer_win == 'Winner':
        computer_wins +=1
        print(f"Computer has won {computer_wins} matches!")
        print('#' * 50)
    else:
        print("Nobody wins!")
        print('#' * 50)
# when either the computer or player has won 3 games the while loop will exit
print('The game has ended! Well played')
# Printing the match game report
gamefunctions_kh.write_report(match_report, player_wins, computer_wins)

