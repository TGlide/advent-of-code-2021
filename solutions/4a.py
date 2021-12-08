from utils import getInputFileLines


def hasWonBingo(board, numbers):
    rows = board
    cols = [[row[i] for row in board] for i in range(len(board))]

    for row in rows:
        if all(num in numbers for num in row):
            return row

    for col in cols:
        if all(num in numbers for num in col):
            return col

    return False


def printBoard(board):
    for row in board:
        print(' '.join([str(num) for num in row]))


if __name__ == "__main__":
    lines = getInputFileLines('4')

    bingo_numbers = [int(n) for n in lines[0].split(',')]

    boards = []
    curr_board = []
    for line in lines[1:]:
        if len(line.strip()) == 0:
            boards.append(curr_board)
            curr_board = []
        else:
            curr_board.append([int(n) for n in line.split()])
    boards.append(curr_board)

    for ub in range(len(bingo_numbers)):
        print('Bingo numbers:', bingo_numbers[:ub])

        for board in boards:
            winning_numbers = hasWonBingo(board, bingo_numbers[:ub])
            if winning_numbers:
                print('\nBINGO!')
                print('Winning numbers:', winning_numbers)
                print('\nBoard:')
                printBoard(board)

                unmarked_numbers = []
                for row in board:
                    unmarked_numbers.extend(
                        [num for num in row if num not in bingo_numbers[:ub]])

                print(unmarked_numbers)
                print(sum(unmarked_numbers) * bingo_numbers[ub-1])

                exit(0)
