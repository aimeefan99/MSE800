import hashlib

import decorators
from decorators import login_required

animals = ["Lion", "Elephant", "Zebra"]
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

#   The admin_login function takes a username and password as arguments and checks if they match the predefined admin credentials. 
#   If the login is successful, it sets the admin_logged_in variable to True, allowing access to the protected functions. 
#   If the login fails, it prints an error message.
def admin_login(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if username == ADMIN_USERNAME and password_hash == ADMIN_PASSWORD_HASH:
        decorators.admin_logged_in = True
        print("Admin login successful.")
    else:
        print("Invalid username or password.")

#   The view_animals function is decorated with @login_required, which means it can only be accessed if the admin is logged in. 
#   It prints the list of animals currently in the zoo.
@login_required
def view_animals():
    print("Zoo animals:", ", ".join(animals))

#   The add_animal function is also decorated with @login_required, ensuring that only logged-in admins can add new animals to the zoo.
#   It takes an animal name as an argument, adds it to the animals list, and prints a confirmation message.
@login_required
def add_animal(animal):
    animals.append(animal)
    print(f"{animal} added to the zoo.")
