import csv
from datetime import timedelta
from package import Package
from truck import Truck
from hash_table import HashTable

h_table = HashTable()
HUB = "4001 South 700 East"
first_truck = Truck(16, 18, None, 0.0, HUB, timedelta(hours=8))
second_truck = Truck(16, 18, None, 0.0, HUB, timedelta(hours=10, minutes=20))
third_truck = Truck(16, 18, None, 0.0, HUB, timedelta(hours=9, minutes=5))

# Read Package CSV data file
with open('./csv_data_files/package_data.csv') as file:
    csv_file = list(csv.reader(file, delimiter=','))

    # Loop through package data
    for row in csv_file:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_deadline = row[5]
        weight = row[6]
        special_note = row[7]

        # Create a new package instance from the current row of the package data
        package = Package(id, address, city, state, zip, delivery_deadline,
                            weight, special_note)
        
        # Change the address of Package #9 to 410 S St. as stated in assumptions 
        if package.get_id() == 9:
            package.set_address("410 S State St")
            package.set_zip("84111")
        
        # Manually/heuristically load packages on the truck based on assumptions
        # First truck packages
        if (package.get_id() == 1 or package.get_id() == 13 or package.get_id() == 14 or package.get_id() == 15 or package.get_id() == 16 or package.get_id() == 19 or
                        package.get_id() == 20 or package.get_id() == 29 or package.get_id() == 30 or package.get_id() == 31 or package.get_id() == 34 or 
                        package.get_id() == 37 or package.get_id() == 40):
            
            # Set package truck number, then load package onto truck
            package.set_truck_num("First Truck")
            first_truck.load_package(package)

        # Second Truck packages
        if (package.get_id() == 3 or package.get_id() == 12 or package.get_id() == 17 or package.get_id() == 18 or 
                        package.get_id() == 21 or package.get_id() == 22 or package.get_id() == 23 or package.get_id() == 24 or package.get_id() == 26 or package.get_id() == 27 or 
                        package.get_id() == 35 or package.get_id() == 36 or package.get_id() == 38 or package.get_id() == 39):
            
            # Set package truck number, then load package onto truck
            package.set_truck_num("Second Truck")
            second_truck.load_package(package)

        # Whatever packages are left go on the third (final) truck
        if (package.get_id() == 2 or package.get_id() == 4 or package.get_id() == 5 or package.get_id() == 6 or package.get_id() == 7 or package.get_id() == 8 or package.get_id() == 9 or 
                        package.get_id() == 10 or package.get_id() == 11 or package.get_id() == 25 or package.get_id() == 28 or package.get_id() == 32 or package.get_id() == 33):
            
            # Set package truck number, then load package onto truck
            package.set_truck_num("Third Truck")
            third_truck.load_package(package)
        
        # Store packages in the custom hash table
        h_table.insert(package.get_id(), package)


# Return the customer hash table full of package data
def get_h_table():
    return h_table

# Get the first truck data
def get_first_truck():
    return first_truck

# Get the second truck data
def get_second_truck():
    return second_truck

# Get the third truck data
def get_third_truck():
    return third_truck


# print(get_h_table())
# print("First Truck")
# print(get_first_truck())
# print("\n\n")
# print("Second Truck")
# print(get_second_truck())
# print("\n\n")
# print("Third Truck")
# print(get_third_truck())
# print("\n\n")