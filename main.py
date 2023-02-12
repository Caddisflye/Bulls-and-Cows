"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jiri Steif
email: jiristeif (zavinac) seznam.cz
discord: Caddi#3130
"""

board = [' ' for x in range(9)]


def print_board():
    """Function for printing out the board state"""
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
    spacer = "+---+---+---+"

    print()
    print(spacer)
    print(row1)
    print(spacer)
    print(row2)
    print(spacer)
    print(row3)
    print(spacer)
    print()


def get_valid_user_choice():
    """gets the user choice and validate it"""
    choice = None
    while choice is None:
        input_value = input("Enter your move (1-9): ").strip()
        try:
            choice = int(input_value)
            if choice not in range(1, 10):
                choice = None
                print(f"{input_value} is not a valid choice. Please enter a number between 1 and 9")
        except ValueError:
            print(f"{input_value} is not a valid choice. Please enter a number between 1 and 9")

    return choice


def player_move(icon):
    """get user move and apply it to board"""
    spacer = "============================================"
    print(spacer)
    print(f"Your turn player {icon}")
    choice = get_valid_user_choice()

    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")
    print(spacer)


def is_victory(icon):
    """checks the board state, if a player wins, return True, else return False"""
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    """checks the board state for draw"""
    if ' ' not in board:
        return True
    else:
        return False


def fancy_print(text):
    """simple function to print text surrounded by '=' to make it stand out"""
    print("============================================")
    print(text)
    print("============================================")


if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    game_rules = """============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game!
--------------------------------------------"""
    print(game_rules)
    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory('X'):
            fancy_print("Player X wins! Congratulations!")
            break
        elif is_draw():
            fancy_print("It's a draw!")
            break
        player_move('O')
        if is_victory('O'):
            print_board()
            fancy_print("Player O wins! Congratulations!")
            break
        elif is_draw():
            print_board()
            fancy_print("It's a draw!")
            break
