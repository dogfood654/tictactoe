import pygame, sys
from random import randrange
import time

# initialise game
pygame.init()

# initialise colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# set screen size
screen_width = 720
screen_height = 480

# set surface for board
board_size = 320
board_surface = pygame.Surface((board_size, board_size))

# calculate center of screen
screen_center = (
    (screen_width-board_size)/2,
    (screen_height-board_size)/2
)

# display screen
pygame.display.set_caption("Feng's Tic-tac-toe")
screen = pygame.display.set_mode((screen_width, screen_height))

# draw board
box_size = 100
line_thickness = 10
vertical1 = (100, 0)
vertical2 = (210, 0)
horizontal1 = (0, 100)
horizontal2 = (0, 210)

# set screen and surface color
screen.fill(black)
board_surface.fill(white)

# draw board
def draw_board(board):

    pygame.draw.rect(board_surface, black, pygame.Rect(vertical1 + (line_thickness, board_size)))
    pygame.draw.rect(board_surface, black, pygame.Rect(vertical2 + (line_thickness, board_size)))
    pygame.draw.rect(board_surface, black, pygame.Rect(horizontal1 + (board_size, line_thickness)))
    pygame.draw.rect(board_surface, black, pygame.Rect(horizontal2 + (board_size, line_thickness)))

    for box in range(len(board)):
        if board[box] != " ":
            pos_y = box // 3
            pos_x = box % 3
            if board[box] == "O":
                pygame.draw.circle(board_surface, blue, (50 + pos_x*110, 50 + pos_y*110), 45)
                pygame.draw.circle(board_surface, white, (50 + pos_x*110, 50 + pos_y*110), 38)
            if board[box] == "X":
                pygame.draw.line(board_surface, red, (10 + pos_x*110, 10 + pos_y*110), (90 + pos_x*110, 90 + pos_y*110), 10)
                pygame.draw.line(board_surface, red, (10 + pos_x*110, 90 + pos_y*110), (90 + pos_x*110, 10 + pos_y*110), 10)

def draw_winningline():
    # check horizontal
    if current_board[0] == current_board[1] == current_board[2] != " ":
        pygame.draw.line(board_surface, green, (0, 50), (320, 50), 10)
    elif current_board[3] == current_board[4] == current_board[5] != " ":
        pygame.draw.line(board_surface, green, (0, 160), (320, 160), 10)
    elif current_board[6] == current_board[7] == current_board[8] != " ":
        pygame.draw.line(board_surface, green, (0, 270), (320, 270), 10)
    # check vertical
    elif current_board[0] == current_board[3] == current_board[6] != " ":
        pygame.draw.line(board_surface, green, (50, 0), (50, 320), 10)
    elif current_board[1] == current_board[4] == current_board[7] != " ":
        pygame.draw.line(board_surface, green, (160, 0), (160, 320), 10)
    elif current_board[2] == current_board[5] == current_board[8] != " ":
        pygame.draw.line(board_surface, green, (270, 0), (270, 320), 10)
    # check diagonal
    elif current_board[0] == current_board[4] == current_board[8] != " ":
        pygame.draw.line(board_surface, green, (0, 0), (320, 320), 10)
    elif current_board[2] == current_board[4] == current_board[6] != " ":
        pygame.draw.line(board_surface, green, (0, 320), (320, 0), 10)
    screen.blit(board_surface, screen_center)
    pygame.display.update()

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

def normal_check():
    # check horizontal
    if current_board[0] == current_board[1] == current_board[2] != " ":
        return "end"
    elif current_board[3] == current_board[4] == current_board[5] != " ":
        return "end"
    elif current_board[6] == current_board[7] == current_board[8] != " ":
        return "end"
    # check vertical
    elif current_board[0] == current_board[3] == current_board[6] != " ":
        return "end"
    elif current_board[1] == current_board[4] == current_board[7] != " ":
        return "end"
    elif current_board[2] == current_board[5] == current_board[8] != " ":
        return "end"
    # check diagonal
    elif current_board[0] == current_board[4] == current_board[8] != " ":
        return "end"
    elif current_board[2] == current_board[4] == current_board[6] != " ":
        return "end"
    # check still going or draw
    else:
        for i in range(len(current_board)):
            if current_board[i] == ' ':
                return "going"
        return "draw"

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

def game_over():

    my_font = pygame.font.SysFont("times new roman", 50)
    game_over_surface = my_font.render("End game", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/2)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()


# game conditions
current_board = [   " ", " ", " ",
                    " ", " ", " ",
                    " ", " ", " "  ]
who_turn = "X"
# for minimax purpose
player_turn = "O"
strategy = "min"
value = 999
optimal_slot = 999

# run game
while True:

    # computer input
    if normal_check() == "going":
        if who_turn == "X":
            filled = 0
            for i in current_board:
                if i != " ":
                    filled += 1
            if filled == 0:
                ai_move = randrange(9)
            else:
                value, ai_move = minimax(current_board, player_turn, strategy, value, optimal_slot)
            current_board[ai_move] = "X"
            who_turn = "O"

    # update surface
    draw_board(current_board)
    screen.blit(board_surface, screen_center)
    pygame.display.update()
    if normal_check() == "end":
        draw_winningline()
        game_over()
    if normal_check() == "draw":
        game_over()

    # player input
    surface_pos = []
    if normal_check() == "going":
        blank_space = []
        for i in range(len(current_board)):
            if current_board[i] == " ":
                blank_space.append(i)
        answer = 9
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                surface_pos = list(pos)
                surface_pos[0] -= screen_center[0]
                surface_pos[1] -= screen_center[1]
        try:
            if surface_pos[0] in range(0, 100) and surface_pos[1] in range(0, 100):
                answer = 0
            elif surface_pos[0] in range(110, 210) and surface_pos[1] in range(0, 100):
                answer = 1
            elif surface_pos[0] in range(220, 320) and surface_pos[1] in range(0, 100):
                answer = 2
            elif surface_pos[0] in range(0, 100) and surface_pos[1] in range(110, 210):
                answer = 3
            elif surface_pos[0] in range(110, 210) and surface_pos[1] in range(110, 210):
                answer = 4
            elif surface_pos[0] in range(220, 320) and surface_pos[1] in range(110, 210):
                answer = 5
            elif surface_pos[0] in range(0, 100) and surface_pos[1] in range(220, 320):
                answer = 6
            elif surface_pos[0] in range(110, 210) and surface_pos[1] in range(220, 320):
                answer = 7
            elif surface_pos[0] in range(220, 320) and surface_pos[1] in range(220, 320):
                answer = 8
        except:
            pass
        # dont allow overlap
        if answer in blank_space:
            current_board[answer] = "O"
            who_turn = "X"

    # update surface
    draw_board(current_board)
    screen.blit(board_surface, screen_center)
    pygame.display.update()
    if normal_check() == "end":
        game_over()
    if normal_check() == "draw":
        game_over()
