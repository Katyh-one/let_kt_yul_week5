# outcome
# Draw
# rock and rock - decision1 = decision2
# paper and paper
# scissors and scissors
# player1 wins
# rock and scissors - decision1 = 'Rock' and decision2 = 'Scissors' - player1 win
# paper and rock - decision1 = 'Paper' and decision2 = 'Rock' - player1 win
# scissors and paper - decision1 = 'Scissors' and decision2 = 'Paper' - player1 win
# computer wins
# rock and paper - decision1 = 'Rock' and decision2 = 'Paper' - computer wins
# paper and scissors - decision1 = 'Paper' and decision2 = 'Scissors' - computer wins
# scissors and rock - decision1 = 'Scissors' and decision2 = 'Rock' - computer win

# function to validate that the user has entered the correct input
def validate_user():
    player1_outcomes = ['R', 'P', 'S']
    while True:
        player1 = input('1, 2, 3 GO - Type R or P or S: ').upper()
        if player1 not in player1_outcomes:
            print('Please enter a valid value - R, P, S')
        else:
            return player1


# function to convert the player input into comparable string
def player_convert(player_input):
    if player_input == 'R':
        player1 = 'Rock'

    elif player_input == 'P':
        player1 = 'Paper'

    else:
        player1 = 'Scissors'
    return player1


# function to convert computer decision into comparable string
def computer_convert(computer):
    if computer == '0':
        computer = 'Rock'

    elif computer == '1':
        computer = 'Paper'

    else:
        computer = 'Scissors'
    return computer


# function to compare the strings and output values to then total the wins and loses
def compare_outcomes(player1, computer):
    # putting the winning combinations into a dictionary that can later be called in the if statement
    winning_combinations = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }
    # if (player1 == 'Rock' and computer == 'Scissors') or ( player1 == 'Paper' and computer == 'Rock')
    # or ( player1 == 'Scissors' and computer == 'Paper'):
    # uses player1 value as they key and then retrieves the associated value
    # if the value matches the computer value then player wins
    if winning_combinations[player1] == computer:
        player_win = 'Winner'
        computer_win = 'Loser'
        print('You have beaten computer!!')
    # elif (player1 == 'Rock' and computer == 'Paper') or ( player1 == 'Paper' and computer == 'Scissors')
    # or (player1 == 'Scissors' and computer == 'Rock'):
    # uses computer value as the key and then retrieves the associated value
    # if the value matches the player value then computer wins
    elif winning_combinations[computer] == player1:
        player_win = 'Loser'
        computer_win = 'Winner'
        print(f"Sorry player one you have lost!")
    else:
        player_win = 'Next time'
        computer_win = 'Next time'
        print(f"It's a draw - go again?")
    return player_win, computer_win


# function to write to the new file created with the ending match report
def write_report(match_report, player_wins, computer_wins):
    match_report.write('Match Report \n' + ('*' * 50) + '\n')
    match_report.write('Good game! Well played!\n')
    match_report.write('Total Wins')
    match_report.write(f'\nPlayer 1: {player_wins} \nComputer: {computer_wins}')
    match_report.close()
    with open('matchreport.txt', 'r') as file:
        for line in file:
            print(line[:-1])


if __name__ == "__main__":
    result = player_convert('S')
    print(result)
    another_result = computer_convert('0')
    print(another_result)
    compare_outcomes('Rock', 'Scissors')
