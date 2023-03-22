from .trip import Trip

class NationalPark:

    def __init__(self, name):
        if type(name) == str:
            self.name = name

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else:
            print("cannot change name")

    def trips(self):
        trip_list = []
        for trip in Trip.all:
            if trip.national_park == self:
                trip_list.append(trip)
        return trip_list

    def visitors(self):
        visitor_list = []
        for trip in self.trips():
            if trip.visitor not in visitor_list:
                visitor_list.append(trip.visitor)
        return visitor_list

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        from .trip import Trip
        count_obj = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in count_obj:
                    count_obj[trip.visitor] = 1
                else:
                    count_obj[trip.visitor] += 1
        most_trips = max(count_obj, key = count_obj.get)
        return most_trips
