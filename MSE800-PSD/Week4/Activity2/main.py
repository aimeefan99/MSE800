from rectangle import Rectangle

# Get user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Create rectangle object
rect = Rectangle(length, width)

# Display results
rect.print_dimensions()
print(f"Area: {rect.calculate_area()}")
print(f"Perimeter: {rect.calculate_perimeter()}")