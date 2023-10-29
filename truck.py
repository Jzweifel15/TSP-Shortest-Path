from hash_table import HashTable

class Truck:

    # Truck Constructor
    def __init__(self, capacity, speed, load, mileage, address, departure_time):
        self.packages = []
        self.capacity = capacity
        self.speed = speed 
        self.load = load
        self.mileage = mileage 
        self.address = address 
        self.departure_time = departure_time
        self.time = departure_time


    # Print a string representation of a Truck object
    def __str__(self):
        return f"Capacity={self.capacity}, Speed={self.speed}, Load={self.load}, Packages={self.packages}, Mileage={self.mileage}, Address={self.address}, Departure_Time={self.departure_time}"

    # Add a new package to a truck
    def load_package(self, package):
        self.packages.append(package)

    # Getter and Setter methods for all Package attributes
    # Get all the packages loaded on a particular truck
    def get_packages(self):
        return self.packages
    
    # Getter/Setter for Capacity
    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    # Getter/Setter for Speed
    def get_speed(self):
        return self.speed
    
    def set_speed(self, new_speed):
        self.speed = new_speed

    # Getter/Setter for Load
    def get_load(self):
        return self.load
    
    def set_load(self, new_load):
        self.load = new_load

    # Getter/Setter for Mileage
    def get_mileage(self):
        return float(self.mileage)
    
    def set_mileage(self, new_mileage):
        self.mileage = new_mileage

    # Getter/Setter for Address
    def get_address(self):
        return self.address
    
    def set_address(self, new_address):
        self.address = new_address

    # Getter/Setter for Departure_Time
    def get_departure_time(self):
        return self.departure_time
    
    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    # Getter/Setter for Time
    def get_time(self):
        return self.time
    
    def set_time(self, new_time):
        self.time = new_time

