"""Command-line interaction helpers for tic-tac-toe."""

from game_rules import check_winner, create_board, is_draw, switch_player


def display_board(board):
    """Print the board in a simple 3x3 grid."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def display_positions():
    """Show the board position numbers for user input."""
    print("Board positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")


def get_player_move(board, player):
    """Prompt the current player until a valid move is entered."""
    while True:
        choice = input(f"Player {player}, choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice)
        if position < 1 or position > 9:
            print("Position must be between 1 and 9.")
            continue

        if board[position - 1] != " ":
            print("That position is already taken.")
            continue

        return position - 1


def play_game():
    """Run one full game of tic-tac-toe."""
    board = create_board()
    current_player = "X"

    print("Welcome to Tic-tac-toe.")
    print("Two players take turns using X and O.")
    display_positions()

    while True:
        display_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins.")
            break

        if is_draw(board):
            display_board(board)
            print("The game is a draw.")
            break

        current_player = switch_player(current_player)


def run_cli():
    """Start the game and offer replay."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break
