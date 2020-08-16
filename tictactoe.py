import math

board = [[' ' for i in range(0, 3)] for j in range(0, 9, 3)]
print('---------')
for i in board:
    print('| {} |'.format(' '.join(i)))
print('---------')
step_turn_sign = 'X'
step_count = 0
while True:
    x, y = input('Enter the coordinates: ').split()
    # check if user input is numbers
    if x.isnumeric() and y.isnumeric():
        x = int(x)
        y = int(y)
    else:
        print('You should enter numbers!')
        continue
    # check if coordinates in the field
    if x not in range(1, 4) or y not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        continue
    # check if cell is empty
    column = x - 1
    row = 3 - y
    if board[row][column] == ' ':
        board[row][column] = step_turn_sign
        print('---------')
        for i in board:
            print('| {} |'.format(' '.join(i)))
        print('---------')
        step_count += 1
    else:
        print('This cell is occupied! Choose another one!')
        continue
    match = []
    # check for lines
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            match.append(step_turn_sign)
    # check for columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            match.append(step_turn_sign)
    # check for diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        match.append(step_turn_sign)
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        match.append(step_turn_sign)
    # result printing
    if len(match) > 1 or math.fabs(board.count('X') - board.count('O')) > 1:
        print('Impossible')
        continue
    elif len(match) == 0 and ' ' in board:
        print('Game not finished')
        continue
    elif len(match) == 0 and ' ' not in board and step_count == 9:
        print('Draw')
        break
    elif len(match) == 1:
        print('{} wins'.format(match[0]))
        break
    if step_turn_sign == 'X':
        step_turn_sign = 'O'
    else:
        step_turn_sign = 'X'
