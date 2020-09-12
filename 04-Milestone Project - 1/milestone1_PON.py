# Milestone project 1: TICTACTOE
# Written by: Paul O'Neill

import time
import os
clear = lambda: os.system('cls')

def choose_marker():
    p1 = input("Player 1: Choose 'x' or 'o': ").lower()
    if p1 == 'x':
        p2 = 'o'
    elif p1 == 'o':
        p2 = 'x'
    else:
        print(f"{p1} is not an 'x' or an 'o'")
        p1 = 'x'
        p2 = 'o'
        print(f'Autoset: Player 1 = {p1}, Player 2 = {p2}')
        time.sleep(2)
    return {'Player 1':p1,'Player 2':p2}

def draw_board(player, pos, board):
    '''
    Inputs: player, new position, and current board
    Ouputs: new board
    pos==0 returns empty board, pos==10 returns board with markers
    '''
    empty = "\n   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
    positions = "\n 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 "

    if board == '':
        board = empty

    if pos == 0:
        # empty board
        return empty
    elif pos == 10:
        # display positions on the board
        return positions
    elif pos in range(1,10):
        spltidx = positions.index(str(pos))
        splitbrd = [board[:spltidx],board[spltidx+1:]]
        board = player.join(splitbrd)
        return board
    
def winner(board):
    positions = "\n 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 "
    win_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]

    # build array of position indices in string
    pos = []
    for i in range(1,10):
        pos.append(positions.index(str(i)))

    # replace element in win combinations with the corresponding string element in board
    for i, combo in enumerate(win_combinations):
        for j in range(0,len(combo)):
            win_combinations[i][j] = board[pos[win_combinations[i][j]-1]]

    # search for exes or ohs in win_combinations
    exes = ['x','x','x']
    ohs = ['o','o','o']
    if exes in win_combinations:
        win = (True, 'x')
    elif ohs in win_combinations:
        win = (True, 'o')
    else: win = (False, '')
    return win

# MAIN
play = True
clear()
i = 0

while play:
    try:
        play = input('Would you like to play TICTACTOE? (y/n): ') == 'y'
        clear()
        if not play: break
        i+=1
        # choose players
        p = choose_marker()
        board = ''

        for move in range(1,7):
            for player in p.keys():
                try:
                    clear()
                    # draw board with markers
                    print(draw_board('',10,''))
                    print(board)
                    pos = int(input(f'\n{player}: make your move: '))
                    board = draw_board(p[player],pos,board)
                    win = winner(board)
                    if win[0]:
                        clear()
                        print(board)
                        print(f'\n{win[1].upper()} WINS!!\n')
                        break
                    if move >= 6:
                        clear()
                        print(board)
                        print('DRAW!')
                except KeyboardInterrupt:
                    break
            if win[0]:
                break
    except KeyboardInterrupt:
        break

if i != 0:
    print('\nThank you for playing\n')
else: print('FUCK OFF SO')
print('Goodbye\n')
time.sleep(1)
clear()