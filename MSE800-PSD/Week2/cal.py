# Check the value of round(45.5)
# Python uses banker's rounding: rounds to nearest even in case of ties
result = round(45.5)
print(f"round(45.5) = {result}")

# Let's also check a few more examples
print(f"round(44.5) = {round(44.5)}")  # Should be 44 (even)
print(f"round(45.5) = {round(45.5)}")  # Should be 46 (even)
print(f"round(46.5) = {round(46.5)}")  # Should be 46 (even)