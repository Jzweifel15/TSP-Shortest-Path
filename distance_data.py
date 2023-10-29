import csv

# Read Distance CSV file
with open('./csv_data_files/distance_data.csv') as file:
    csv_file = list(csv.reader(file, delimiter=','))

    # Put all distance data into a list - creating a 2D-list
    def load_distance_data():
        return csv_file
   

# print(load_distance_data())