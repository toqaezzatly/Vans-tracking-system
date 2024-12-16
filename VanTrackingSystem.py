import datetime
import random

'''Base class for vans'''
class Vehicle:
    def __init__(self, vanID, make, model, registration):
        self.vanID = vanID
        self.make = make
        self.model = model
        self.registration = registration
        self.currentLocation = (0, 0)  # -> (x, y)
        self.speed = 0
        self.last_update = datetime.datetime.now()
        self.odometer = 0

    def update_location(self, x, y):
        self.currentLocation = (x, y)
        self.last_update = datetime.datetime.now()

    def update_speed(self, speed):
        self.speed = speed
        self.last_update = datetime.datetime.now()

    def update_odometer(self, odometer):
        self.odometer = odometer
        self.last_update = datetime.datetime.now()

    def get_status(self):
        return {
            "vanID": self.vanID,
            "make": self.make,
            "model": self.model,
            "registration": self.registration,
            "currentLocation": self.currentLocation,
            "speed": self.speed,
            "last_update": self.last_update,
            "odometer": self.odometer
        }

    def __str__(self):
        return f"Vehicle {self.vanID} - {self.make} {self.model} ({self.registration})"


class Van(Vehicle):
    def __init__(self, vanID, make, model, registration, maxload):
        super().__init__(vanID, make, model, registration)
        self.maxload = maxload
        '''initial load'''
        self.currentload = 0

    def load_cargo(self, weight):
        if self.currentload + weight <= self.maxload:
            self.currentload += weight
            return f'Loaded {weight}kg of cargo to van {self.vanID}, current load: {self.currentload}kg'
        else:
            return f'Cannot load {weight}kg of cargo to van {self.vanID}   EXCEEDS MAX LOAD, current load: {self.currentload}kg'

    def unload_cargo(self, weight):
        if self.currentload - weight >= 0:
            self.currentload -= weight
            return f'Unloaded {weight}kg of cargo from van {self.vanID}, current load: {self.currentload}kg'
        else:
            return f'Cannot unload {weight}kg of cargo from van {self.vanID}   EXCEEDS CURRENT LOAD, current load: {self.currentload}kg'

    def get_status(self):
        van_status = super().get_status()
        van_status["maxload"] = self.maxload
        van_status["currentload"] = self.currentload
        return van_status


class Track:
    def __init__(self):
        self.vans = {}

    def add_van(self, van):
        self.vans[van.vanID] = van

    def get_van_status(self, vanID):
        if vanID in self.vans:
            status = self.vans[vanID].get_status()
            print(f"Status for van {vanID}:")
            for key, value in status.items():
                print(f"  {key}: {value}")
            return
        print(f'Van {vanID} not found')

    def update_van_location(self, vanID, x, y):
        if vanID in self.vans:
            self.vans[vanID].update_location(x, y)
            return f'Updated location of van {vanID} to ({x}, {y})'
        return f'Van {vanID} not found'

    def update_van_speed(self, vanID, speed):
        if vanID in self.vans:
            self.vans[vanID].update_speed(speed)
            return f'Updated speed of van {vanID} to {speed} km/h'
        return f'Van {vanID} not found'

    def update_van_odometer(self, vanID, odometer):
        if vanID in self.vans:
            self.vans[vanID].update_odometer(odometer)
            return f'Updated odometer of van {vanID} to {odometer} km'
        return f'Van {vanID} not found'

    def get_all_van_statuses(self):
        status_list = []
        for van_id in self.vans:
            status = self.vans[van_id].get_status()
            print(f"Status for van {van_id}:")
            for key, value in status.items():
                print(f"  {key}: {value}")
            status_list.append(status)
        return status_list

if __name__ == "__main__":
    track = Track()
    van1 = Van(1, "Toyota", "Camry", "ABC123", 1000)
    van2 = Van(2, "Honda", "Civic", "XYZ789", 800)
    track.add_van(van1)
    track.add_van(van2)
    print(track.update_van_location(1, 10, 20))
    print(track.update_van_speed(1, 60))
    print(track.update_van_odometer(1, 5000))
    print(track.update_van_location(2, 30, 40))
    print(track.update_van_speed(2, 70))
    print(track.update_van_odometer(2, 6000))
    track.get_van_status(1)
    track.get_van_status(2)
    track.get_all_van_statuses()