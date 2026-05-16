admin_logged_in = False

#   The login_required decorator is used to restrict access to certain functions unless the admin is logged in.
def login_required(func):
    # This is the wrapper function that will be returned by the decorator.
    def wrapper(*args, **kwargs):
        #   The wrapper checks if the admin_logged_in variable is True before allowing access to the decorated function.
        if not admin_logged_in:
            print("Access denied. Please log in first.")
            return
        #  If the admin is logged in, the wrapper calls the original function with the provided arguments and returns its result.
        return func(*args, **kwargs) 
    return wrapper #    The login_required function returns the wrapper function, which is what gets executed when the decorated function is called.
