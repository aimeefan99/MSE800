class Flight:
    # Parent class for shared flight information.
    def __init__(self, flight_number, departure, destination, carry_on_allowance, checked_baggage_allowance):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.carry_on_allowance = carry_on_allowance
        self.checked_baggage_allowance = checked_baggage_allowance

    def show_route(self):
        return f"{self.flight_number}: {self.departure} -> {self.destination}"

    def show_baggage(self):
        return f"Carry-on: {self.carry_on_allowance} | Checked bag: {self.checked_baggage_allowance}"

    def show_summary(self):
        return f"{self.show_route()} | {self.show_baggage()}"


class DomesticFlight(Flight):
    # Domestic flights share local check-in rules.
    def flight_type(self):
        return "Domestic"

    def check_in_info(self):
        return "Online check-in is available. ID may be checked for bag drop or manual check-in."

    def show_domestic_rule(self):
        return f"{self.flight_type()} rule: {self.check_in_info()}"


class InternationalFlight(Flight):
    # International flights share visa rules.
    def flight_type(self):
        return "International"

    def check_visa(self):
        return "Required"

    def show_international_rule(self):
        return f"{self.flight_type()} rule: Visa {self.check_visa()}"


class DirectFlight:
    # Direct flights do not have stopovers.
    def flight_mode(self):
        return "Direct"

    def show_stop_info(self):
        return "No stopover"

    def travel_note(self):
        return "Go directly to your departure gate."


class TransitFlight:
    # Transit flights include a stopover.
    def __init__(self, stopover):
        self.stopover = stopover

    def flight_mode(self):
        return "Transit"

    def show_stop_info(self):
        return f"Stopover: {self.stopover}"

    def travel_note(self):
        return "Check the next boarding gate during transit."


class DomesticDirectFlight(DomesticFlight, DirectFlight):
    def show_details(self):
        return f"{self.show_summary()} | Type: {self.flight_type()} {self.flight_mode()}"

    def show_full_trip(self):
        return f"{self.show_details()} | {self.show_stop_info()}"

    def show_summary(self):
        return f"{self.show_route()} | {self.show_baggage()}"


class DomesticTransitFlight(DomesticFlight, TransitFlight):
    def __init__(self, flight_number, departure, destination, carry_on_allowance, checked_baggage_allowance, stopover):
        DomesticFlight.__init__(
            self,
            flight_number,
            departure,
            destination,
            carry_on_allowance,
            checked_baggage_allowance,
        )
        TransitFlight.__init__(self, stopover)

    def show_details(self):
        return f"{self.show_summary()} | Type: {self.flight_type()} {self.flight_mode()}"

    def show_full_trip(self):
        return f"{self.show_details()} | {self.travel_note()}"

    def show_summary(self):
        return f"{self.show_route()} | {self.show_baggage()} | {self.show_stop_info()}"


class InternationalDirectFlight(InternationalFlight, DirectFlight):
    def show_details(self):
        return (
            f"{self.show_summary()} | Type: {self.flight_type()} {self.flight_mode()} | "
            f"Visa: {self.check_visa()}"
        )

    def show_full_trip(self):
        return f"{self.show_details()} | {self.show_stop_info()}"

    def show_summary(self):
        return f"{self.show_route()} | {self.show_baggage()}"


class InternationalTransitFlight(InternationalFlight, TransitFlight):
    def __init__(self, flight_number, departure, destination, carry_on_allowance, checked_baggage_allowance, stopover):
        InternationalFlight.__init__(
            self,
            flight_number,
            departure,
            destination,
            carry_on_allowance,
            checked_baggage_allowance,
        )
        TransitFlight.__init__(self, stopover)

    def show_details(self):
        return (
            f"{self.show_summary()} | Type: {self.flight_type()} {self.flight_mode()} | "
            f"Visa: {self.check_visa()}"
        )

    def show_full_trip(self):
        return f"{self.show_details()} | {self.travel_note()}"

    def show_summary(self):
        return f"{self.show_route()} | {self.show_baggage()} | {self.show_stop_info()}"


def main():
    domestic_direct = DomesticDirectFlight("NZ101", "Auckland", "Wellington", "7kg", "Depends on fare")
    domestic_transit = DomesticTransitFlight(
        "NZ202",
        "Auckland",
        "Queenstown",
        "7kg",
        "Depends on fare",
        "Christchurch",
    )
    international_direct = InternationalDirectFlight(
        "NZ289",
        "Auckland",
        "Shanghai",
        "7kg",
        "2 bags x 23kg",
    )
    international_transit = InternationalTransitFlight(
        "NZ777",
        "Auckland",
        "London",
        "7kg",
        "2 bags x 23kg",
        "Singapore",
    )

    print("Air New Zealand Flight Management System")
    print(domestic_direct.show_full_trip())
    print(domestic_direct.check_in_info())
    print(domestic_transit.show_full_trip())
    print(international_direct.show_full_trip())
    print(international_transit.show_full_trip())


if __name__ == "__main__":
    main()
