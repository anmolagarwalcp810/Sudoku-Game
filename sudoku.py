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


def print_board(board):
    length_of_board = len(board[0])
    for i in range(length_of_board):
        if (i in [3, 6]):
            print("\n-----------------------------")
        else:
            print('')
        for j in range(length_of_board):
            if (j in [3, 6]):
                print("|", end=' '),
            print(str(board[i][j]), end=' '),


print_board(board)


def find_in_line(b, i, j, n):  # flag=0, corresponds to row, flag1 corresponds to column
    length_of_board = len(b[0])

    for k in range(length_of_board):
        if (n == b[i][k]):
            return True

    for k in range(length_of_board):
        if (n == b[k][j]):
            return True

    n1 = (i // 3) * 3  # base row
    n2 = (j // 3) * 3  # base row

    for k in range(n1, n1 + 3):
        for l in range(n2, n2 + 3):
            if (n == b[k][l]):
                return True

    return False


def get_ones_and_zeros(board):
    length_of_board = len(board[0])
    one_zero_board = []
    for i in range(length_of_board):
        temp_line = [0 for k in range(length_of_board)]
        for j in range(length_of_board):
            if (board[i][j] > 0):
                temp_line[j] = 1
        one_zero_board += [temp_line]
    return one_zero_board


def solve_sudoku(board, one_zero_board):
    i = 0
    length_of_board = len(board[0])
    # i corresponds to row, j corresponds to column
    set_j = 0
    backtrack = False
    while (i < length_of_board):
        j = set_j
        print("++++++++++++++++++++++++++++++++++++++++")
        print_board(board)
        print("")
        #print(str(backtrack))
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
                    if (find_in_line(board, i, j, k)):
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
    return board


one_zero_board = get_ones_and_zeros(board)

solved_board = solve_sudoku(board, one_zero_board)

print("\n\nSolved board")

print_board(solved_board)
