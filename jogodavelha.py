def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn % 2]

        print_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                row = int(input("Enter row number (1, 2, 3): "))
                col = int(input("Enter column number (1, 2, 3): "))
                if is_valid_move(board, row, col):
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        turn += 1

        if turn == 9:
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
