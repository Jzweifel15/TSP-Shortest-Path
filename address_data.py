import csv

# Read Address CSV file
with open('./csv_data_files/address_data.csv') as file:
    csv_file = list(csv.reader(file, delimiter=','))

    # Load the address data for later use
    def load_address_data():
        return csv_file


# print(load_address_data())