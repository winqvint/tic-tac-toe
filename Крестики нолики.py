print('Добро пожаловать в игру "крестики-нолики" ')
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board(board):
    print('_' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('_' * 13)


def player_turn_input(player):
    while True:
        try:
            turn = int(input(f'Игрок {player}, выбери позицию от (1-9): ')) - 1
            if turn < 0 or turn > 8:
                print('Выберите позицию от 1 до 9')
            elif str(board[turn]) in ("X", "O"):
                print('Эта клетка уже занята! Попробуйте другую.')
            else:
                board[turn] = player
                break
        except (ValueError, IndexError):
            print('Неверный ввод! Введите число от 1 до 9.')


def check_win(player):
    win_combinations = [
        [0, 1, 2],  # Горизонтальные линии
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Вертикальные линии
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Диагонали
        [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_draw():
    return all(isinstance(i,str)for i in board)


def play_game():
    current_player = 'X'
    while True:
        draw_board(board)
        player_turn_input(current_player)

        if check_win(current_player):
            draw_board(board)
            print(f'Игрок {current_player} победил!')
            break

        if check_draw():
            draw_board(board)
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()