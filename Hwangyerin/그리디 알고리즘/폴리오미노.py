board = list(input())
len_board = len(board)
idx = 0

while idx < len_board:
    if ''.join(board[idx:idx+4]) == 'XXXX':
        board[idx:idx+4] = ['A', 'A', 'A', 'A']
        idx += 4
    elif ''.join(board[idx:idx+2]) == 'XX':
        board[idx:idx+2] = ['B', 'B']
        idx += 2
    elif board[idx] == 'X':
        board = -1
        break
    else:
        idx += 1

if board == -1:
    print(board)
else:
    print(''.join(board))