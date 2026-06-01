# Week8 - Activity 4: Hybrid Inheritance - Air New Zealand

This project extends Activity 3 into a more complete Air New Zealand flight management system. It models:

- Domestic direct flights
- Domestic transit flights
- International direct flights
- International transit flights

The design demonstrates **hybrid inheritance** by combining:

- `Hierarchical inheritance`
- `Multilevel inheritance`
- `Multiple inheritance`

## Class Structure

```text
Flight
├── DomesticFlight
│   ├── DomesticDirectFlight
│   └── DomesticTransitFlight
└── InternationalFlight
    ├── InternationalDirectFlight
    └── InternationalTransitFlight

DirectFlight
├── DomesticDirectFlight
└── InternationalDirectFlight

TransitFlight
├── DomesticTransitFlight
└── InternationalTransitFlight
```

## Why It Is Hybrid Inheritance

- `Flight -> DomesticFlight` and `Flight -> InternationalFlight` show hierarchical inheritance.
- `Flight -> DomesticFlight -> DomesticDirectFlight` and `Flight -> InternationalFlight -> InternationalTransitFlight` show multilevel inheritance.
- Classes such as `DomesticDirectFlight(DomesticFlight, DirectFlight)` use multiple inheritance.

## Class Diagram

```text
+-------------------------------+
|            Flight             |
+-------------------------------+
| flight_number                 |
| departure                     |
| destination                   |
| carry_on_allowance            |
| checked_baggage_allowance     |
+-------------------------------+
| show_route()                  |
| show_baggage()                |
| show_summary()                |
+-------------------------------+
           ^                                     ^
           |                                     |
+----------------------+        +----------------------+
|    DomesticFlight    |        |  InternationalFlight|
+----------------------+        +----------------------+
|                      |        |                      |
+----------------------+        +----------------------+
| flight_type()        |        | flight_type()        |
| check_in_info()      |        | check_visa()         |
| show_domestic_rule() |        | show_international_rule() |
+----------------------+        +----------------------+
           ^         ^                    ^         ^
           |         |                    |         |
+----------------------+        +----------------------+
|    DirectFlight      |        |    TransitFlight     |
+----------------------+        +----------------------+
|                      |        | stopover             |
+----------------------+        +----------------------+
| flight_mode()        |        | flight_mode()        |
| show_stop_info()     |        | show_stop_info()     |
| travel_note()        |        | travel_note()        |
+----------------------+        +----------------------+
      ^           ^                    ^           ^
      |           |                    |           |
+------------------------+   +------------------------+
| DomesticDirectFlight   |   | DomesticTransitFlight  |
+------------------------+   +------------------------+
| show_details()         |   | show_details()         |
| show_full_trip()       |   | show_full_trip()       |
| show_summary()         |   | show_summary()         |
+------------------------+   +------------------------+

+---------------------------+ +-----------------------------+
| InternationalDirectFlight | | InternationalTransitFlight  |
+---------------------------+ +-----------------------------+
| show_details()            | | show_details()              |
| show_full_trip()          | | show_full_trip()            |
| show_summary()            | | show_summary()              |
+---------------------------+ +-----------------------------+
```

## Files

- `main.py` - Python implementation with `main()`
- `class_diagram.md` - Mermaid class diagram
- `class_diagram.drawio` - draw.io class diagram

## Run

```bash
python3 main.py
```

## Sample Output

```text
Air New Zealand Flight Management System
NZ101: Auckland -> Wellington | Carry-on: 7kg | Checked bag: Depends on fare | Type: Domestic Direct | No stopover
Online check-in is available. ID may be checked for bag drop or manual check-in.
NZ202: Auckland -> Queenstown | Carry-on: 7kg | Checked bag: Depends on fare | Stopover: Christchurch | Type: Domestic Transit | Check the next boarding gate during transit.
NZ289: Auckland -> Shanghai | Carry-on: 7kg | Checked bag: 2 bags x 23kg | Type: International Direct | Visa: Required | No stopover
NZ777: Auckland -> London | Carry-on: 7kg | Checked bag: 2 bags x 23kg | Stopover: Singapore | Type: International Transit | Visa: Required | Check the next boarding gate during transit.
```