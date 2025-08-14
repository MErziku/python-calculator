# Step 1: Create an empty list called my_list
my_list = []  # This creates an empty list
print("Empty list:", my_list)  # Let's print to see what it looks like

# Step 2: Append elements 10, 20, 30, 40 to my_list
my_list.append(10)  # Adds 10 to the end
my_list.append(20)  # Adds 20 to the end
my_list.append(30)  # Adds 30 to the end
my_list.append(40)  # Adds 40 to the end
print("After appending:", my_list)  # Check our progress

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)  # Inserts 15 at position 1 (second spot)
print("After inserting 15:", my_list)

# Step 4: Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])  # Adds all elements from the new list
print("After extending:", my_list)

# Step 5: Remove the last element
my_list.pop()  # Removes and returns the last item (we don't need to save it)
print("After removing last element:", my_list)

# Step 6: Sort in ascending order
my_list.sort()  # Sorts the list in place
print("After sorting:", my_list)

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)  # Finds the position of 30
print("Index of 30:", index_of_30)