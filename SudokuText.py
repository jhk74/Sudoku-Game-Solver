# sudoku solver with text only

sudokuBoard = [[0, 0, 0, 6, 0, 0, 4, 0, 0],
               [7, 0, 0, 0, 0, 3, 6, 0, 0],
               [0, 0, 0, 0, 9, 1, 0, 8, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 5, 0, 1, 8, 0, 0, 0, 3],
               [0, 0, 0, 3, 0, 6, 0, 4, 5],
               [0, 4, 0, 2, 0, 0, 0, 6, 0],
               [9, 0, 3, 0, 0, 0, 0, 0, 0],
               [0, 2, 0, 0, 0, 0, 1, 0, 0]]


def printBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def isEmpty(bo):
    rows = len(bo)
    cols = len(bo[0])
    for i in range(rows):
        for j in range(cols):
            if bo[i][j] == 0:
                return (i, j)

    return None


def isValid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    posx = pos[0] - pos[0] % 3
    posy = pos[1] - pos[1] % 3
    for j in range(posx, posx + 3):
        for k in range(posy, posy + 3):
            if bo[j][k] == num and (j, k) != pos:
                return False

    return True


def solveBoard(bo):
    pairs = isEmpty(bo)
    if not pairs:
        return True
    else:
        row, col = pairs
    for i in range(1, 10):
        if isValid(bo, i, (row, col)):
            bo[row][col] = i

            if solveBoard(bo):
                return True
            bo[row][col] = 0

    return False


printBoard(sudokuBoard)
solveBoard(sudokuBoard)
printBoard(sudokuBoard)

