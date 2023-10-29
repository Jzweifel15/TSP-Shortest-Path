class Package:

    # Constructor for a package object
    def __init__(self, id, address, city, state, zip, delivery_deadline, 
                    weight, special_note):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_note = special_note
        self.departure_time = ''
        self.delivery_time = ''
        self.delivery_status = ''
        self.truck_num = ''

    # Print a string representation of a Package object
    def __str__(self):
        return f"ID={self.id}, Address={self.address}, City={self.city}"

    # Getter and Setter methods for all Package attributes
    # Getter/Setter for ID
    def get_id(self):
        return int(self.id)
    
    def set_id(self, new_id):
        self.id = new_id

    # Getter/Setter for Address
    def get_address(self):
        return self.address
    
    def set_address(self, new_address):
        self.address = new_address

    # Getter/Setter for City
    def get_city(self):
        return self.city
    
    def set_city(self, new_city):
        self.city = new_city

    # Getter/Setter for State
    def get_state(self):
        return self.state
    
    def set_state(self, new_state):
        self.state = new_state

    # Getter/Setter for Zip
    def get_zip(self):
        return self.zip
    
    def set_zip(self, new_zip):
        self.zip = new_zip

    # Getter/Setter for Delivery Deadline
    def get_delivery_deadline(self):
        return self.delivery_deadline
    
    def set_delivery_deadline(self, new_delivery_deadline):
        self.delivery_deadline = new_delivery_deadline

    # Getter/Setter for Weight
    def get_weight(self):
        return self.weight
    
    def set_weight(self, new_weight):
        self.weight = new_weight

    # Getter/Setter for Special Notes
    def get_special_note(self):
        return self.special_note
    
    def set_special_note(self, new_special_note):
        self.special_note = new_special_note

    # Getter/Setter for Delivery Status
    def get_delivery_status(self):
        return self.delivery_status
    
    def set_delivery_status(self, new_delivery_status):
        self.delivery_status = new_delivery_status

    # Getter/Setter for Departure Time
    def get_departure_time(self):
        return self.departure_time
    
    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    # Getter/Setter for Delivery Time
    def get_delivery_time(self):
        return self.delivery_time
    
    def set_delivery_time(self, new_delivery_time):
        self.delivery_time = new_delivery_time

    # Getter/Setter for Truck Number
    def get_truck_num(self):
        return self.truck_num
    
    def set_truck_num(self, new_truck_num):
        self.truck_num = new_truck_num

