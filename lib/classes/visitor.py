from .trip import Trip

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            if type(name) == str and 1 <= len(name) <= 15:
                self._name = name
        else:
            print("name must be of type string and between 1 and 15 letters long")

    def trips(self):
        trip_list = []
        for trip in Trip.all:
            if trip.visitor == self:
                trip_list.append(trip)
        return trip_list

    def nationalparks(self):
        park_list = []
        for trip in self.trips():
            if trip.national_park not in park_list:
                park_list.append(trip.national_park)
        return park_list

    def create_trip(self, national_park, start_date, end_date):
        Trip(self, national_park, start_date, end_date)