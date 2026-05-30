class Flight:
    # Parent class: shared information for any flight.
    def __init__(self, flight_number, departure, destination):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination

    def show_route(self):
        return f"{self.flight_number}: {self.departure} -> {self.destination}"


class DomesticFlight(Flight):
    # Domestic flights do not need visa checks.
    def __init__(self, flight_number, departure, destination):
        super().__init__(flight_number, departure, destination)
        self.baggage_allowance = 7

    def show_details(self):
        return (
            f"{self.show_route()} | Domestic | "
            f"Baggage: {self.baggage_allowance}kg | Visa: Not required"
        )


class InternationalFlight(Flight):
    # International flights need visa checks and more baggage allowance.
    def __init__(self, flight_number, departure, destination):
        super().__init__(flight_number, departure, destination)
        self.baggage_allowance = 23

    def check_visa(self):
        return "Required"

    def show_details(self):
        return (
            f"{self.show_route()} | International | "
            f"Baggage: {self.baggage_allowance}kg | Visa: {self.check_visa()}"
        )


domestic_flight = DomesticFlight("NZ101", "Auckland", "Wellington")
international_flight = InternationalFlight("NZ289", "Auckland", "China")

print("Air New Zealand Flight System")
print(domestic_flight.show_details())
print(international_flight.show_details())
