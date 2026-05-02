# Rectangular Land OOP Project

This is a simple object-oriented Python project for calculating the area and perimeter of a rectangular piece of land.

## What the project includes

### rectangle.py
- Contains the `Rectangle` class
- The class stores the length and width of the land
- It has three methods:
  - `calculate_area()` to calculate the area
  - `calculate_perimeter()` to calculate the perimeter
  - `print_dimensions()` to display the dimensions

### main.py
- Runs the program
- Takes user input for length and width
- Creates an object of the `Rectangle` class
- Displays the dimensions, area, and perimeter

## OOP concepts used

- **Class**: `Rectangle`
- **Object**: Created in main.py as `rect`
- **Methods**: `calculate_area()`, `calculate_perimeter()`, and `print_dimensions()`

## How the code works

1. The user enters the length
2. The user enters the width
3. The program creates a `Rectangle` object
4. The program calculates:
   - Area = length × width
   - Perimeter = 2 × (length + width)
5. The results are printed on the screen

## How to run

Use this command in the project folder:

```bash
python3 main.py
```

## Example

```
Enter length: 10
Enter width: 15
Length: 10.0, Width: 15.0
Area: 150.0
Perimeter: 50.0
```

## Summary

This project is a beginner-friendly OOP example. It uses one class and multiple methods across two Python files, which matches the activity requirement.