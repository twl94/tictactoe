board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(3):
        print(
            " "+board[i*3] + " | "
            + board[i*3+1] + " | "
            + board[i*3+2] + " | "
        )
        if i < 2:
            print("---|---|---")

    print()

def check_winner(player):
    win_pos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in win_pos:
        if all(board[i] == player for i in line):
            return True
    return False

turn = "X"
for _ in range(9):
    print_board()
    move = int(input(f'{turn}의 차례입니다. (0~8)'))


    if move > 8:
        print("범위를 벗어났습니다. 0부터 8까지 선택해주세요.")
        continue
    elif board[move] != " ":
        print('이미 선택된 칸입니다.')
        continue

    board[move] = turn

    if check_winner(turn):
        print_board()
        print(f'{turn} 승리')
        break

    turn = "O" if turn == "X" else "X"
    
else:
    print_board()
    print("무승부")
