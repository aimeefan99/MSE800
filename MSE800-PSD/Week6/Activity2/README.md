# Zoo Application - Admin Login

## Project Structure

- `main.py`: runs the program
- `zoo_admin.py`: contains the admin functions
- `decorators.py`: contains the `login_required` decorator

## Functionality

This project is a simple Zoo Application for an admin user.
The admin must log in before viewing or adding animals.
The password is checked using a stored hash instead of plain text.

## Decorator

The `login_required` decorator is defined in `decorators.py`.
It checks whether the admin is logged in.
If the admin is not logged in, access is denied.
If the admin is logged in, the function runs normally.

## How to Run

Run the program with:

```bash
python main.py
```

Then enter:
- admin username
- admin password
- a new animal name

## Example Output

```text
Enter admin username: admin
Enter admin password: ****
Admin login successful.
Zoo animals: Lion, Elephant, Zebra
Enter a new animal: Giraffe
Giraffe added to the zoo.
Zoo animals: Lion, Elephant, Zebra, Giraffe
```
