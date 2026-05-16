#   This is the main file for the zoo administration project.
#  It will import the necessary functions from the zoo_admin module and execute them in a sequence to demonstrate the admin login activities, including viewing and adding animals to the zoo.
from zoo_admin import admin_login, view_animals, add_animal

#   This is the main function that will execute the admin login activities.
def main():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    admin_login(username, password)
    view_animals()
    animal = input("Enter a new animal: ")
    add_animal(animal)
    view_animals()

#   This will ensure that the main function is called when the script is executed.
if __name__ == "__main__":
    main()
