# Zoo Application - Admin Login

## Project Structure

- `main.py`: runs the program
- `zoo_admin.py`: contains the admin functions
- `decorators.py`: contains the `login_required` decorator

## Functionality

This project is a simple Zoo Application for an admin user.
The admin needs to log in before using the protected zoo functions.
After a successful login, the admin can:
- view the current animal list
- add a new animal
- view the updated animal list

The project also improves the login process by checking a stored password hash
instead of comparing a plain text password directly in the code.

## Decorator

The `login_required` decorator is defined in `decorators.py`.
It checks the variable `admin_logged_in` before running a function.
If the admin is not logged in, access is denied.
If the admin is logged in, the original function runs normally.

This decorator is used for:
- `view_animals()`
- `add_animal(animal)`

This means the admin must log in first before viewing or changing zoo data.

## Program Flow

The program follows this order:
1. The user enters the admin username and password.
2. The system checks the login details.
3. If login is successful, the current animal list is shown.
4. The user enters a new animal.
5. The animal is added to the list.
6. The updated animal list is shown.

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
