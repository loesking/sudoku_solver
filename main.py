test_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(board: list) -> None:
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - ')

        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


def find_empty_field(board: list) -> tuple:
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if board[i][j] == 0:
                return i, j


def validate_value(board: list, num: int, pos: tuple) -> bool:
    for i, row in enumerate(board):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i, row in enumerate(board):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_board(board: list) -> bool:
    empty_field = find_empty_field(board)
    if not empty_field:
        return True
    else:
        row, col = empty_field

    for i in range(1, 10):
        if validate_value(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False


def main():
    print_board(test_board)
    solve_board(test_board)
    print('__________________')
    print_board(test_board)


if __name__ == '__main__':
    main()
