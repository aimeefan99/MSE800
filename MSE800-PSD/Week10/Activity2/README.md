# Week10 - Activity2: Tic-tac-toe Game

This activity is a simple command-line Tic-tac-toe game for two players using object-oriented programming.

## Features

- Two-player game using `X` and `O`
- Command-line input
- Input validation
- Win detection
- Draw detection
- Replay option
- Simple object-oriented design with classes

## Program Structure

- `main.py` is the program entry point.
- `game.py` contains the main classes.
- `Board` stores the board data and checks the board state.
- `TicTacToeGame` controls the game flow and user interaction.

## Game Logic

- A player wins when three same symbols appear in one row, one column, or one diagonal.
- A draw happens when the board is full and no player has won.
- If there are still empty spaces and no winning line, the game continues.

## Run the Program

Run:

   ```bash
   python main.py
   ```

## Pylint Check

![Pylint check result](pylintcheck.png)

## Coding Style

- The code uses simple classes and methods for readability.
- The file is intended to be checked with `pylint` and general PEP8 style rules.
