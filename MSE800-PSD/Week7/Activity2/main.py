from database import create_table
from fish_manager import add_fish, view_all_fish_details, view_fish

# The Fish class represents a fish with attributes such as name, category, color, appearance, size, and age.
class Fish:
    def __init__(self, name, category, color, appearance, size, age): 
        self.name = name
        self.category = category
        self.color = color
        self.appearance = appearance
        self.size = size
        self.age = age

# The factory creates fish objects from user input.
# It is used here to encapsulate the creation of fish objects and to ensure that only valid fish categories are created.
class FishFactory:
    def create_fish(self, name, category, color, appearance, size, age):
        valid_categories = ["goldfish", "shark", "angelfish", "tuna", "salmon"]
        if category not in valid_categories:
            return None
        return Fish(name, category.capitalize(), color, appearance, size, age) 


def menu():
    print("\nAquarium Menu")
    print("1. Add fish")
    print("2. View all fish details")
    print("3. View fish summary")
    print("4. Exit")


def main():
    capacity = 20
    create_table()
    factory = FishFactory()

    while True:
        menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            name = input("Enter fish name: ")
            category = input(
                "Enter fish category (goldfish/shark/angelfish/tuna/salmon): "
            ).lower()
            color = input("Enter fish color: ")
            appearance = input("Enter fish appearance: ")
            size = input("Enter fish size: ")
            age = int(input("Enter fish age: "))

            fish = factory.create_fish(name, category, color, appearance, size, age)

            if fish is None:
                print("Invalid fish category.")
            else:
                added = add_fish(fish, capacity)
                if added:
                    print("Fish added successfully.")

        elif choice == "2":
            rows = view_all_fish_details()
            if not rows:
                print("No fish found.")
            else:
                print("\nAll fish details:")
                for row in rows:
                    print(
                        "Name: "
                        + str(row[0])
                        + ", Category: "
                        + str(row[1])
                        + ", Color: "
                        + str(row[2])
                        + ", Appearance: "
                        + str(row[3])
                        + ", Size: "
                        + str(row[4])
                        + ", Age: "
                        + str(row[5])
                    )

        elif choice == "3":
            rows = view_fish()
            if not rows:
                print("No fish found.")
            else:
                # Show the total number of fish in each category.
                print("\nFish currently available in the aquarium:")
                for row in rows:
                    print("Category: " + str(row[0]) + ", Quantity: " + str(row[1]))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
