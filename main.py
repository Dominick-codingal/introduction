def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    
    for turn in range(9):
        print_board(board)
        player = players[turn % 2]
        
        while True:
            try:
                row = int(input(f"Player {player}, enter row (0, 1, 2): "))
                col = int(input(f"Player {player}, enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("That spot is taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
    
    print_board(board)
    print("It's a tie!")

tic_tac_toe()