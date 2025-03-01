# Tic-Tac-Toe Game in Python

# Function to print the board
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)  # This will now print a full separator line

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (draw)
def board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to handle the game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != " ":
                print("Cell is already occupied! Try again.")
                continue
            board[row][col] = current_player
        except (ValueError, IndexError):
            print("Invalid input! Please enter values between 0 and 2.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
