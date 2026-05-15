# This import statement brings in the datetime class from the datetime module, which is used to work with dates and times in Python. 
# In this code, it is specifically used to log the time when a function is called in the log_activity decorator.
from datetime import datetime 

# This module contains various decorators that can be used to enhance the functionality of functions.
# The log_activity decorator is used to log the activity details whenever a function is called. 
# It prints the function name, the time of execution, and messages indicating the start and completion of the activity
def log_activity(func):

    # This is the wrapper function that will be returned by the decorator. 
    # It takes any number of positional and keyword arguments.
    def wrapper(*args, **kwargs): # *args and **kwargs allow the wrapper to accept any number of arguments and pass them to the original function without modification.
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # This line calls the original function with the provided arguments and stores the result. 
        # The decorator can perform actions before and after this call, allowing it to enhance the original function's behavior without modifying its code.
        result = func(*args, **kwargs) 

        print("Activity completed.")
        print("===================================\n")

        return result
    
    return wrapper
