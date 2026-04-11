# calculate x raised to the power of y
def calculate_power(x, y):
    return x ** y  

# main program entry
def main():
    try:
        # get user input
        x = float(input("Enter base (x): "))
        y = float(input("Enter exponent (y): "))

        # calculate result
        result = calculate_power(x, y)

        # display output
        print(f"{x} to the power of {y} is {result}")

    except ValueError:
        # handle invalid (non-numeric) input
        print("Invalid input. Please enter numeric values.")


# run program only when executed directly
if __name__ == "__main__":
    main()