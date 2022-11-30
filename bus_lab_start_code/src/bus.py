class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger)
    
    def pick_up(self, picked_up_passenger):
        self.passenger.append(picked_up_passenger)

    def drop_off(self, dropped_off_passenger):
        self.passenger.remove(dropped_off_passenger)
    
    def empty(self):
        self.passenger = []
        return len(self.passenger)

    def pick_up_from_stop(self, bus_stop):
        for passengers in bus_stop.queue:
            self.passenger.append(passengers)
        bus_stop.clear()


