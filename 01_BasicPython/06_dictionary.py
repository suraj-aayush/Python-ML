# Dictionary with operations
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing a value by key
name = my_dict["name"]

# Adding a new key-value pair
my_dict["job"] = "Engineer"

# Updating an existing value
my_dict["age"] = 31

# Removing a key-value pair
del my_dict["city"]

# Get all keys, values, and items
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(name)  # Alice
print(my_dict)  # {'name': 'Alice', 'age': 31, 'job': 'Engineer'}
print(keys)  # dict_keys(['name', 'age', 'job'])
print(values)  # dict_values(['Alice', 31, 'Engineer'])
print(items)  # dict_items([('name', 'Alice'), ('age', 31), ('job', 'Engineer')])
