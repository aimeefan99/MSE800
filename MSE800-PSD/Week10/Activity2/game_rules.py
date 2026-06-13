"""Game rules and board helpers for tic-tac-toe."""


def create_board():
    """Create and return an empty 3x3 board."""
    return [" "] * 9


def check_winner(board, player):
    """Return True when the player has a winning line."""
    winning_lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for line in winning_lines:
        if (
            board[line[0]] == player
            and board[line[1]] == player
            and board[line[2]] == player
        ):
            return True
    return False


def is_draw(board):
    """Return True when the board is full and nobody has won."""
    return " " not in board


def switch_player(player):
    """Return the other player's symbol."""
    if player == "X":
        return "O"
    return "X"
