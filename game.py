import pygame
import sudoku
import time

import math

original_board = [
    [0, 0, 9, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 3, 1, 0],
    [0, 6, 1, 0, 0, 8, 0, 5, 0],
    [0, 0, 5, 4, 0, 0, 2, 0, 3],
    [0, 1, 0, 0, 0, 7, 0, 0, 8],
    [0, 8, 0, 0, 0, 0, 7, 6, 0],
    [3, 0, 6, 0, 1, 9, 4, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 5, 0, 6, 2, 7]
]

board = [
    [0, 0, 9, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 3, 1, 0],
    [0, 6, 1, 0, 0, 8, 0, 5, 0],
    [0, 0, 5, 4, 0, 0, 2, 0, 3],
    [0, 1, 0, 0, 0, 7, 0, 0, 8],
    [0, 8, 0, 0, 0, 0, 7, 6, 0],
    [3, 0, 6, 0, 1, 9, 4, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 5, 0, 6, 2, 7]
]

original_one_zero_board = sudoku.get_ones_and_zeros(original_board)

one_zero_board = sudoku.get_ones_and_zeros(board)

# initialise pygame
pygame.init()

side = 600

# create screen
screen = pygame.display.set_mode((542, 542))

# number font
num_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
enter_num_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
game_font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",70)

def draw_rectangles(l, n):  # n is number of blocks, l is side length of one block
    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(i * l, j * l, l, l)
            pygame.draw.rect(screen, (0, 255, 0), rect, 2)

    n1 = n//3
    l1 = l*3

    for i in range(n1+1):
    	for j in range(n1+1):
    		rect = pygame.Rect(i * l1, j * l1, l1, l1)
    		pygame.draw.rect(screen, (0,255,0), rect, 10)

def game_over_display():
    game_text = game_font.render("YOU WIN!", True, (255,255,255))
    screen.blit(game_text, (120, 240))

def show_default_value(n, x, y):
    num_text = num_font.render(str(n), True, (200, 180, 0))
    screen.blit(num_text, (x, y))


def display_temporary_fixed_value(n, x, y):
    num_text = num_font.render(str(n), True, (160, 160, 160))
    screen.blit(num_text, (x, y))


def display_board(board, n, l):
    for i in range(n):
        for j in range(n):
            if (board[i][j] == 0):
                pass
            else:
                if (original_one_zero_board[i][j] == 1):
                    show_default_value(board[i][j], j * l + l / 4, i * l + l / 4)
                elif (one_zero_board[i][j] == 0 and original_one_zero_board[i][j]==0):
                    display_num(board[i][j], j * l + 2 * l / 3, i * l + l / 4)
                elif (one_zero_board[i][j] ==1 and original_one_zero_board[i][j]==0):
                    display_temporary_fixed_value(board[i][j], j * l + l / 4, i * l + l / 4)


def draw_cursor(flag, x, y, l):  # if flag = 0, then yellow, if flag= 1, then red (to indicate wrong answer)
    rect = pygame.Rect(x, y, l, l)
    if flag == 0:
        pygame.draw.rect(screen, (200, 200, 200), rect, 5)
    elif flag == 1:
        pygame.draw.rect(screen, (255, 0, 0), rect, 5)


def display_num(n, x, y):
    enter_num = enter_num_font.render(str(n), True, (160, 160, 160))
    screen.blit(enter_num, (x, y))

def solve_sudoku_with_display(board, one_zero_board):
    i = 0
    length_of_board = len(board[0])
    # i corresponds to row, j corresponds to column
    set_j = 0
    backtrack = False
    while (i < length_of_board):
        j = set_j
        # print("++++++++++++++++++++++++++++++++++++++++")
        # print_board(board)
        # print("")
        # print(str(backtrack))
        while (j < length_of_board):
            if (one_zero_board[i][j] == 1):
                if (backtrack):
                    if (j == 0):
                        set_j = length_of_board - 1
                        i -= 1
                        while (one_zero_board[i][set_j] == 1):
                            if (set_j == 0):
                                set_j = length_of_board - 1
                                i -= 1
                            else:
                                set_j -= 1
                        break
                    else:
                        j -= 1
                else:
                    j += 1
                    if (j == length_of_board):
                        i += 1
                        set_j = 0
            else:
                flag = 0  # will be k if found k is successful, if not we backtrack and set the current to 0
                for k in range(board[i][j] + 1, length_of_board + 1):
                    # print("board[i][j]+1 k "+str(k))
                    if (sudoku.find_in_line(board, i, j, k)):
                        pass
                    else:
                        flag = k
                        break
                if (flag == 0):
                    backtrack = True
                    board[i][j] = 0
                    if (j == 0):
                        set_j = length_of_board - 1
                        i -= 1
                        # keep on setting i and j until we get empty box
                        while (one_zero_board[i][set_j] == 1):
                            if (set_j == 0):
                                i -= 1
                                set_j = length_of_board - 1
                            else:
                                set_j -= 1
                        break
                    else:
                        j -= 1
                else:
                    backtrack = False
                    # print("flag: "+str(flag)+" i: "+str(i)+" j: "+str(j))
                    board[i][j] = flag
                    j += 1
                    if (j == length_of_board):
                        set_j = 0
                        i += 1

        draw_cursor(0, j*60, i*60, 60)
        display_board(board, 9, 60)

    return board

# cursor coordinates
cursor_flag = 0
cursor_X = 60
cursor_Y = 0
cursor_change = 60

#game flag
game_flag = True
not_solved = True

#solved board
solved_board = sudoku.solve_sudoku(original_board,original_one_zero_board)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cursor_X -= cursor_change
                cursor_flag = 0
            elif event.key == pygame.K_RIGHT:
                cursor_X += cursor_change
                cursor_flag = 0
            if event.key == pygame.K_UP:
                cursor_Y -= cursor_change
                cursor_flag = 0
            elif event.key == pygame.K_DOWN:
                cursor_Y += cursor_change
                cursor_flag = 0
            coordinate_X, coordinate_Y = cursor_X // 60, cursor_Y // 60
            if event.key == pygame.K_1:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 1
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_2:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 2
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_3:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 3
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_4:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 4
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_5:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 5
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_6:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 6
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_7:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 7
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_8:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 8
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            elif event.key == pygame.K_9:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    board[coordinate_Y][coordinate_X] = 9
                    one_zero_board[coordinate_Y][coordinate_X] = 0
            if event.key == pygame.K_RETURN:
                n=board[coordinate_Y][coordinate_X]
                board[coordinate_Y][coordinate_X]=0
                print(n)
                if sudoku.find_in_line(board, coordinate_Y, coordinate_X, n):
                    cursor_flag = 1
                    board[coordinate_Y][coordinate_X] = n
                else:
                    one_zero_board[coordinate_Y][coordinate_X] = 1
                    cursor_flag = 0
                    board[coordinate_Y][coordinate_X] = n
            if event.key == pygame.K_DELETE:
                if original_one_zero_board[coordinate_Y][coordinate_X] == 0:
                    one_zero_board[coordinate_Y][coordinate_X] = 0
                    board[coordinate_Y][coordinate_X] = 0
            if event.key == pygame.K_SPACE:
                not_solved = False
                #solve_sudoku_with_display(original_board,original_one_zero_board)

    if cursor_X <= 0:
        cursor_X = 0
    elif cursor_X >= 480:
        cursor_X = 480

    if cursor_Y <= 0:
        cursor_Y = 0
    elif cursor_Y >= 480:
        cursor_Y = 480

    if board == solved_board:
        game_flag = False

    if game_flag and not_solved:
        draw_rectangles(60, 9)
        display_board(board, 9, 60)
        draw_cursor(cursor_flag, cursor_X, cursor_Y, 60)

    elif not game_flag:
        game_over_display()
    else:
        draw_rectangles(60, 9)
        display_board(solved_board, 9, 60)

    pygame.display.update()
