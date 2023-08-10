# Creating a set of room content
room_content = {"net", "table", "bed", "shoerack"}

# Length of the set
print("Length of the room_content:", len(room_content))

# Data type of the set
print("Data type of the room_content:", type(room_content))

# Accessing elements in the set
for item in room_content:
    print("room_content item:", item)

# Adding items to the set
room_content.add("sofa")
room_content.add("lamp")
print("Updated room_content:", room_content)

# Creating another set
additional_set = {"shelf", "mirror"}

# Combining two sets (Union)
combined_set = room_content.union(additional_set)
print("Combined set:", combined_set)
