# Sucessful minimax tictactoe

from random import randrange

# For actual game
board = [   ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '   ]

# For test
current_board = [   ' ', ' ', ' ',
                    ' ', ' ', ' ',
                    ' ', ' ', ' '  ]

# Computer  - X
# Human     - O
# Change this to change who starts
who_turn = 'O' # O means Computer starts first

def display_board(current_board):
    print(current_board[0] + "|" + current_board[1] + "|" + current_board[2])
    print(current_board[3] + "|" + current_board[4] + "|" + current_board[5])
    print(current_board[6] + "|" + current_board[7] + "|" + current_board[8])
    print("")

def human_player(current_board):
    blank_space = []
    for i in range(len(current_board)):
        if current_board[i] == ' ':
            blank_space.append(i)
    answer = 9
    while answer not in blank_space:
        try:
            answer = int(input("Enter a number between 0 and 8: "))
            print("")
        except ValueError:
            print("That is invalid.")
    return answer

def check_board_status(current_board, player_turn):
    # check horizontal
    if current_board[0] == current_board[1] == current_board[2] == player_turn:
        return "end"
    elif current_board[3] == current_board[4] == current_board[5] == player_turn:
        return "end"
    elif current_board[6] == current_board[7] == current_board[8] == player_turn:
        return "end"
    # check vertical
    elif current_board[0] == current_board[3] == current_board[6] == player_turn:
        return "end"
    elif current_board[1] == current_board[4] == current_board[7] == player_turn:
        return "end"
    elif current_board[2] == current_board[5] == current_board[8] == player_turn:
        return "end"
    # check diagonal
    elif current_board[0] == current_board[4] == current_board[8] == player_turn:
        return "end"
    elif current_board[2] == current_board[4] == current_board[6] == player_turn:
        return "end"
    # check still going or draw
    else:
        for i in range(len(current_board)):
            if current_board[i] == ' ':
                return "going"
        return "draw"

# for minimax purposes
player_turn = 'O'
strategy = "min"
value = 999
optimal_slot = 999

def minimax(current_board, player_turn, strategy, value, optimal_slot):
    # Switch turn
    if player_turn == 'X':
        player_turn = 'O'
        strategy = "min"
    else:
        player_turn = 'X'
        strategy = "max"

    # Get blank slots
    blank_space = []
    for i in range(len(current_board)):
        if current_board[i] == ' ':
            blank_space.append(i)

    # Recursion
    value = 999
    optimal_slot = 999
    for i in blank_space:
        current_board[i] = player_turn

        # check win, lose or draw
        status = check_board_status(current_board, player_turn)

        # if no, loop
        if status == "going":
            temp, useless = minimax(current_board, player_turn, strategy, value, optimal_slot)
            if strategy == "max":
                # value = max(value, temp)
                if value == 999:
                    value = temp
                if temp >= value:
                    value = temp
                    optimal_slot = i
            else:
                # value = min(value, temp)
                if value == 999:
                    value = temp
                if temp <= value:
                    value = temp
                    optimal_slot = i
        # if yes, calculate utility
        elif status == "end":
            if player_turn == 'X':
                utility = +1
            else:
                utility = -1 
            temp = utility * len(blank_space)
            if strategy == "max":                
                # value = max(value, temp)
                if value == 999:
                    value = temp
                if temp >= value:
                    value = temp
                    optimal_slot = i
            else:
                # value = min(value, temp)
                if value == 999:
                    value = temp
                if temp <= value:
                    value = temp
                    optimal_slot = i
        else:
            utility = 0
            temp = utility * len(blank_space)
            if strategy == "max":
                # value = max(value, temp)
                if value == 999:
                    value = temp
                if temp >= value:
                    value = temp
                    optimal_slot = i
            else:
                # value = min(value, temp)
                if value == 999:
                    value = temp
                if temp <= value:
                    value = temp
                    optimal_slot = i
        current_board[i] = ' '

    return value, optimal_slot

def main(current_board, who_turn):
    player_turn = 'O'
    strategy = "min"
    value = 999
    optimal_slot = 999

    if who_turn == 'O':
        rand_slot = randrange(9)
        current_board[rand_slot] = 'X'
        who_turn = 'X'

    while check_board_status(current_board, who_turn) == "going":
        if who_turn == 'X':
            who_turn = 'O'
        else:
            who_turn = 'X'
        if who_turn == 'X':
            value, ai_move = minimax(current_board, player_turn, strategy, value, optimal_slot)
            current_board[ai_move] = 'X'
        else:
            display_board(current_board)
            human_move = human_player(current_board)
            current_board[human_move] = 'O'
    if check_board_status(current_board, who_turn) == "end":
        display_board(current_board)
        print(who_turn + " wins!!!")
        print("")
    else:
        display_board(current_board)
        print("Draw!!!")
        print("")

# Run program
main(board, who_turn)

# Tester
# heyhey = minimax(current_board, player_turn, strategy, value, optimal_slot)
# print(heyhey)