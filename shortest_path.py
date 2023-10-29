from address_data import load_address_data as ad
from distance_data import load_distance_data as dd
from package_data import get_h_table
from datetime import timedelta

h_table = get_h_table()

# Get the address index from the name 
def get_address(address):   # O(N)
    for row in ad():
        if address in row[2]:
            return int(row[0])

# print(get_address("4580 S 2300 E"))

# Find the distance between two addresses
def distance_between(address1, address2):   # O(N)
    distance = dd()[address1][address2]
    
    if distance == '':
        distance = dd()[address2][address1]

    return float(distance)


"""
This is the custom shortest path algorithm. This algorithm uses the nearest neighbor method, a type of greedy algorithm. All 
packages are considered "not delivered" (thus, each address (or, "vertex") is considered "unvisited") at the beginning of the 
program. An arbitrary address which each truck/package starts, which is the Hub since all packages/trucks start at the hub at 
the beginning of each day. Then, the algorithm finds the shortest distance from one address (the truck's current address) to 
the next address.Do this for all packages, removing from "not delivered" as to represent that the address (vertex) for the 
package has been visited. 

Space Complexity -> O(1)
Time Complexity -> O(N^2)
"""
def find_shortest_path(truck):
    # Place all non-delivered packages into a list 
    not_delivered = []
    for i in truck.get_packages():          # <-- O(N)
        package = h_table.search(i.get_id())
        not_delivered.append(package)

    # Clear the package list of a given truck so the packages can be placed back into the truck in the order
    # of the nearest neighbor
    truck.get_packages().clear()

    # Cycle through not_delivered until none remain. Add nearest package into the truck, one by one
    while len(not_delivered) > 0:   # <-- Outer[O(N)] * Inner[O(N)] = O(N^2)
        next_address = 100      # Set a base/starting next address for comparing the first address
        next_package = None

        for package in not_delivered:    # <-- O(N)
            if distance_between(get_address(truck.get_address()), get_address(package.get_address())) <= next_address:
                next_address = distance_between(get_address(truck.get_address()), get_address(package.get_address()))
                next_package = package 

        # Adds next closest package to the truck
        truck.load_package(next_package.get_id())

        # Remove the same package from not_delivered
        not_delivered.remove(next_package)

        # Take the mileage driven to deliver the package and add it into the truck's current mileage
        mileage = truck.get_mileage()
        mileage += next_address 
        truck.set_mileage(mileage)

        # Update the truck's current address to the address of the package delivered
        truck.set_address(next_package.get_address())

        # Update the time it took for the truck to drive to the nearest package
        time = truck.get_time()
        time += timedelta(hours=next_address / 18)
        truck.set_time(time)
        next_package.set_delivery_time(truck.get_time())
        next_package.set_departure_time(truck.get_departure_time())


# find_shortest_path(get_first_truck())
# print (distance_between("4001 South 700 East", "195 W Oakland Ave"))
# print(distance_between("195 W Oakland Ave", "2010 W 500 S"))
# print(h_table.size())