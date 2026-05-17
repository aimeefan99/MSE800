#Demonstrate the roles of the underscore (_) in five different ways within a single script to make them clear, along with short comments. Share your GitHub link.
#1. Last Expression in Python
#2.Ignoring Values
#3. As a loop Variable
#4. Formatting Large Numbers
#5. Placeholder for temporary or unimportant variables

# 1. Last Expression in Python Interpreter
a = 1 + 1
_ = a      
print(f"1. Last Expression (_) : {_}")

# 2. Ignoring Values 
first, _, _, _, last = (1,2,3,4,5)
print(f"2. Ignored Middle: First={first}, Last={last}")

# 3. As a loop Variable 
print("3. Loop 5 times: ", end="")  
for _ in range(5):
    print("★")
print()

 # 4. Formatting Large Numbers
money = 1_000_000_000
print(f"4. Large Number: {money}")

# 5. Placeholder for temporary or unimportant variables 
fruits = ["apple", "banana"]
for _, fruit in enumerate(fruits):
    print(f"5. Temporary Placeholder (fruit): {fruit}")