# Aquarium Management

This project manages an aquarium in Auckland with limited space.

## Design Pattern Used

This project uses the `Factory Pattern`.

## Why This Pattern Is Used

The system needs to create fish objects based on the fish category entered by the user, such as `Goldfish`, `Shark`, `Angelfish`, `Tuna`, and `Salmon`.

I used the Factory Pattern because this project needs to create fish objects from user input. The factory creates the object in one place. This is more suitable than Singleton, because Singleton is used to control one instance, while this project mainly needs object creation.

## How It Is Used In This Project

- `Fish` is the main class for fish objects
- `FishFactory` creates a `Fish` object
- the client code sends the fish data to the factory
- the created object is then stored in the SQLite database

It also uses SQLite to store the fish data in 2 tables:

- `fish_categories`
- `aquarium_fish`

Each fish has these attributes:

- `name`
- `category`
- `color`
- `appearance`
- `size`
- `age`

The system can:

- add fish
- view all fish details
- view fish category and quantity

Example output:

```text
Aquarium Menu
1. Add fish
2. View all fish details
3. View fish summary
4. Exit
Select an option (1-4): 1

Enter fish name: Sunny
Enter fish category (goldfish/shark/angelfish/tuna/salmon): goldfish
Enter fish color: Gold
Enter fish appearance: Fancy
Enter fish size: Small
Enter fish age: 1
Fish added successfully.

Aquarium Menu
1. Add fish
2. View all fish details
3. View fish summary
4. Exit
Select an option (1-4): 1
Enter fish name: Storm
Enter fish category (goldfish/shark/angelfish/tuna/salmon): shark
Enter fish color: Grey
Enter fish appearance: Strong
Enter fish size: Large
Enter fish age: 3
Fish added successfully.

Aquarium Menu
1. Add fish
2. View all fish details
3. View fish summary
4. Exit
Select an option (1-4): 3

Fish currently available in the aquarium:
Category: Goldfish, Quantity: 1
Category: Shark, Quantity: 1

Aquarium Menu
1. Add fish
2. View all fish details
3. View fish summary
4. Exit
Select an option (1-4): 4
Goodbye!
```
