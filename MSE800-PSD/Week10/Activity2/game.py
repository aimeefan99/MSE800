"""Object-oriented tic-tac-toe game classes."""


class Board:
    """Store and manage the tic-tac-toe board."""

    def __init__(self):
        """Create an empty board."""
        self.cells = [" "] * 9

    def display(self):
        """Print the current board."""
        print()
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("---+---+---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("---+---+---")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print()

    def is_position_free(self, position):
        """Return True when the chosen position is empty."""
        return self.cells[position] == " "

    def place_mark(self, position, player):
        """Place the player's mark on the board."""
        self.cells[position] = player

    def check_winner(self, player):
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
                self.cells[line[0]] == player
                and self.cells[line[1]] == player
                and self.cells[line[2]] == player
            ):
                return True
        return False

    def is_draw(self):
        """Return True when the board is full."""
        return " " not in self.cells


class TicTacToeGame:
    """Run the command-line tic-tac-toe game."""

    def __init__(self):
        """Set up a new game."""
        self.board = Board()
        self.current_player = "X"

    def display_positions(self):
        """Show the board position numbers."""
        print("Board positions:")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")

    def get_player_move(self):
        """Prompt until the current player enters a valid move."""
        while True:
            choice = input(
                f"Player {self.current_player}, choose a position (1-9): "
            ).strip()

            if not choice.isdigit():
                print("Please enter a number from 1 to 9.")
                continue

            position = int(choice)
            if position < 1 or position > 9:
                print("Position must be between 1 and 9.")
                continue

            index = position - 1
            if not self.board.is_position_free(index):
                print("That position is already taken.")
                continue

            return index

    def switch_player(self):
        """Change to the other player."""
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play(self):
        """Run one full game."""
        print("Welcome to Tic-tac-toe.")
        print("Two players take turns using X and O.")
        self.display_positions()

        while True:
            self.board.display()
            move = self.get_player_move()
            self.board.place_mark(move, self.current_player)

            if self.board.check_winner(self.current_player):
                self.board.display()
                print(f"Player {self.current_player} wins.")
                break

            if self.board.is_draw():
                self.board.display()
                print("The game is a draw.")
                break

            self.switch_player()

    def run(self):
        """Start the program and offer replay."""
        while True:
            self.board = Board()
            self.current_player = "X"
            self.play()

            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print("Goodbye.")
                break
