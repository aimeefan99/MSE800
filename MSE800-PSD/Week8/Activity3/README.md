# Activity 8 - Activity 3: Inheritance - Air New Zealand

This project shows inheritance using an Air New Zealand flight system with both domestic and international routes.

## Class Diagram

```text
+----------------------+
|        Flight        |
+----------------------+
| flight_number        |
| departure            |
| destination          |
+----------------------+
| show_route()         |
+----------------------+
           ^                    ^
           |                    |
+----------------------+
|    DomesticFlight    |
+----------------------+
| baggage_allowance=7  |
+----------------------+
| show_details()       |
+----------------------+

+----------------------+
|  InternationalFlight |
+----------------------+
| baggage_allowance=23 |
+----------------------+
| check_visa()         |
| show_details()       |
+----------------------+
```

## Files

- `main.py` - Python code for the parent class and subclasses
- `class_diagram.md` - Mermaid class diagram

## How It Works

- `Flight` is the parent class.
- `DomesticFlight` inherits shared attributes and methods from `Flight`.
- `InternationalFlight` also inherits shared attributes and methods from `Flight`.
- Domestic flights have a basic baggage allowance and do not need a visa.
- International flights have a larger baggage allowance and return `Required` from `check_visa()`.
- `show_route()` is inherited from the parent class.
- `DomesticFlight` has its own `show_details()` method.
- `InternationalFlight` has `check_visa()` and `show_details()`.

## Run

```bash
python3 main.py
```

## Sample Output

```text
Air New Zealand Flight System
NZ101: Auckland -> Wellington | Domestic | Baggage: 7kg | Visa: Not required
NZ289: Auckland -> China | International | Baggage: 23kg | Visa: Required
```

## GitHub Link

Add your GitHub repository link here after pushing the files.
