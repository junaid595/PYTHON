# Dictionary operations
student = {"name": "Rahul", "age": 20}

print("Original Dictionary:", student)

# Add / append an item
student["course"] = "Python"
print("After adding:", student)

# Update an item
student["age"] = 21
print("After updating:", student)

# Remove an item
student.pop("course")
print("After removing:", student)


# Tuple operations
numbers = (10, 20, 30)

print("\nOriginal Tuple:", numbers)

# Append - create a new tuple
numbers = numbers + (40,)
print("After adding:", numbers)

# Remove - create a new tuple
numbers = tuple(x for x in numbers if x != 20)
print("After removing 20:", numbers)


