# Justin R. Zweifel
# Student ID: 010756930 

from package_data import get_first_truck, get_second_truck, get_third_truck, get_h_table
from shortest_path import find_shortest_path
from datetime import timedelta
import datetime

first_truck = get_first_truck()
second_truck = get_second_truck()
third_truck = get_third_truck()

# Run trucks through the algorithm
find_shortest_path(first_truck)
find_shortest_path(second_truck)

# Ensure that truck 3 does not leave until either of the first two trucks are finished delivering their packages
# Then, run truck 3 through the algorithm
third_truck.set_departure_time(min(first_truck.get_time(), second_truck.get_time()))
find_shortest_path(third_truck)

# Prints the package information in the main program
def print_package_info(package, delivery):
    print(
        f"\nPackage ID: {package.get_id()}\n"
        f"Delivery Address: {package.get_address()}\n"
        f"Delivery City: {package.get_city()}\n"
        f"Delivery Zipcode: {package.get_zip()}\n"
        f"Delivery Deadline: {package.get_delivery_deadline()}\n"
        f"Package Weight: {package.get_weight()}\n"
        f"Package is/was on: {package.get_truck_num()}\n"
        f"Delivery Status: {package.get_delivery_status()}\n"
        f"Delivery Time: {delivery}"
    )

# Determiens which packages have left the Hub, are out for delivery, and/or have been delivered
def determine_package_details(package, time_td, departure, delivery):
    # Find which packages have left the hub
    if departure >= time_td:
        package.set_delivery_status("At the Hub")
        print_package_info(package, delivery)

    # Determine which packages have left, but have not been delivered
    elif departure <= time_td:
        if time_td < delivery:
            package.set_delivery_status("Out for Delivery")
            print_package_info(package, delivery)

        # Determine which packages have already been delivered
        else:
            package.set_delivery_status("Delivered")
            print_package_info(package, delivery)


class Main:
    # Create a user interface in the terminal for user to interact with the program
    print('******************************')
    print('*                            *')
    print('*   WGUPS Delivery Program   *')
    print('*                            *')
    print('******************************\n')
    print(f'Truck 1 traveled {round(first_truck.get_mileage(), 2)} miles.')
    print(f'Truck 2 traveled {round(second_truck.get_mileage(), 2)} miles.')
    print(f'Truck 3 traveled {round(third_truck.get_mileage(), 2)} miles.')
    print(f'All packages were delivered in {first_truck.get_mileage() + second_truck.get_mileage() + third_truck.get_mileage()} miles.\n')

    flag = True

    # While the 'flag' remains True (user has not typed 'Q' or 'q'), keep the program running
    while flag:
        user_input = input("""
Select an option below to begin the program:
    1. Get All Package Statuses with a Time       
    2. Get a Single Package Status with a Time
    'Q' or 'q' to quit the program
""")

        # Check if user wants to end the program
        if user_input == 'q' or user_input == 'Q':
            print("Exiting the program...")
            print("Thank you for trusting WGUPS Delivery!")
            flag = False
        
        # User Selected Option 1
        elif user_input == '1':
            try:
                # Get a specific time from the user to check the statuses of packages
                input_time = input("Enter a time (Format -> HH:MM:SS): ")
                (hr, min, sec) = input_time.split(':')
                time_td = timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

                # Loop through the hash table of packages starting from 1 to the total number of items
                # in the hash table, plus 1 since range's upper limit is exlusive. Note that `i` will represent
                # the package ID which is used to search the hash table
                for i in range(1, get_h_table().size() + 1):
                    try:
                        # Search the hash table for the current iteration; returns a package 
                        package = get_h_table().search(int(i))

                        # Get departure and delivery times for the package of the current iteration
                        departure = package.get_departure_time()
                        delivery = package.get_delivery_time()

                    except ValueError:
                        continue

                    # Custom method that determines the statuses of the packages and prints the information
                    determine_package_details(package, time_td, departure, delivery)

            # Jump back to the beginning prompt if an invalid entry was received
            except ValueError:
                print("Invalid time entry. Make sure to follow the time format provided.")
                continue

        # User Selected Option 2
        elif user_input == '2':
            try:
                # Get a specific package ID from the user to check the status
                input_id = input("Enter the package ID: ")

                # Search the hash table for the package with the provided ID
                # Get departure and delivery times for the package
                package = get_h_table().search(int(input_id))
                departure = package.get_departure_time()
                delivery = package.get_delivery_time()

                # Have the user enter a time for which the requested package status will be compared
                input_time = input("Enter a time (Format -> HH:MM:SS): ")
                (hr, min, sec) = input_time.split(':')
                time_td = timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

                # Custom method that determines the statuses of the packages and prints the information
                determine_package_details(package, time_td, departure, delivery)

            # Jump back to the beginning prompt if an invalid entry was received
            except ValueError:
                print("Entry does not seem to be a valid package ID. Please, try again.")
                continue

        # User has typed an invalid option
        else:
            print("Option not recognized...")
