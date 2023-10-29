class HashTable:

    # Constructor with optional initial capacity parameter
    # Assigns all buckets with an empty list
    def __init__(self, capacity=20):
        # initialize the hash table with empty bucket list entries
        self.table = []
        self.num_items = 0
        for i in range(capacity):
            self.table.append([])   # [[], [], [], [], [], [], [], [], [], []..]

    # Print a string representation of a HashTable
    def __str__(self):
        return f"{self.table}"


    # Function used for hashing an item's key
    def create_hash(self, key):
        return hash(key) % len(self.table)


    # HashTable insertion of new item into the hash table
    def insert(self, key, item):
        # Hash the key
        # Get the bucket list where this item will go
        bucket = self.create_hash(key)
        bucket_list = self.table[bucket]

        # Update key if it is already in the bucket
        for i in bucket_list:
            if i[0] == key:
                i[1] = item 
                return True

        # If not, insert the item to the end of the bucket list
        bucket_list.append([key, item])
        self.num_items += 1
        return True

    
    # Searches for an item with matching key in the hash table
    # Returns the item if found, or None if not found
    def search(self, key):
        # Hash the key
        bucket = self.create_hash(key)

        # Search for the key in the bucket list
        # Find the item's index and return the item that is in the bucket list
        for pair in self.table[bucket]:
            if pair[0] == key:
                return pair[1]
        else:
            # the key is not found
            return None


    # Keep track of the number of items in the hash table
    def size(self):
        return self.num_items
    

# h_table = HashTable()

# package_1 = Package(1, "123 Main St.", "Columbus", "OH", "43209", "EOD", "44", "None")
# h_table.insert(package_1.id, package_1)
# # print(h_table)
# # print("\n")

# package_2 = Package(2, "123 Main St.", "Cincinnati", "OH", "43209", "EOD", "44", "None")
# h_table.insert(package_2.id, package_2)
# # print(h_table)
# # print("\n")

# package_3 = Package(3, "123 Main St.", "Las Angeles", "OH", "43209", "EOD", "44", "None")
# h_table.insert(package_3.id, package_3)
# # print(h_table)
# # print("\n")

# package_10 = Package(10, "456 E Main St.", "San Francisco", "OH", "43209", "10:30", "11", "Can only be on truck 2")
# h_table.insert(package_10.id, package_10)
# # print(h_table)
# # print("\n")

# package_11 = Package(11, "456 E Main St.", "Seattle", "OH", "43209", "10:30", "11", "Can only be on truck 2")
# h_table.insert(package_11.id, package_11)
# # print(h_table)
# # print("\n")

# package_12 = Package(12, "456 E Main St.", "Bellevue", "OH", "43209", "10:30", "11", "Can only be on truck 2")
# h_table.insert(package_12.id, package_12)
# # print(h_table)
# # print("\n")

# package_25 = Package(25, "456 E Main St.", "Chicago", "OH", "43209", "10:30", "11", "Can only be on truck 2")
# h_table.insert(package_25.id, package_25)
# # print(h_table)
# # print("\n")

# package_37 = Package(37, "456 E Main St.", "Detroit", "OH", "43209", "10:30", "11", "Can only be on truck 2")
# h_table.insert(package_37.id, package_37)
# # print(h_table)
# # print("\n")

# package_40 = Package(40, "456 E Main St.", "Washington D.C.", "OH", "43209", "10:30", "11", "Can only be on truck 2")
# h_table.insert(package_40.id, package_40)
# # print(h_table)
# # print("\n")

# print(h_table)
# # # print(f"Size: {h_table.size()}\n\n")

# # print("\n")
# print(h_table.search(40))