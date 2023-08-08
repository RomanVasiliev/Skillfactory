def draw_board(board):
    print("  0 1 2")
    for i in range(3):
        row = " ".join(board[i])
        print(f"{i} {row}")

def check_winner(board):
    for i in range(3):
        # проверка строки
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        # проверка конки
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # проверка деагонали
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def play_game():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"
    winner = None
    while not winner:
        draw_board(board)
        row = int(input(f"Играет {current_player}, введите номер строки: "))
        col = int(input(f"Играет {current_player}, введите номер колонки: "))
        if board[row][col] != " ":
            print("Ячейка занята. Попробуйте еще.")
            continue
        board[row][col] = current_player
        winner = check_winner(board)
        current_player = "O" if current_player == "X" else "X"
    draw_board(board)
    print(f"Поздравляем, игрок {winner} победил!")

play_game()