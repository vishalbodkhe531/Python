# Creating a dictionary
student = {
    "name": "Vishal",
    "age": 20,
    "course": "BCA",
    "is_graduated": False
}

# Accessing values
print(student["name"])         
print(student.get("age"))      

# Updating a value
student["age"] = 21

# Adding a new key-value pair
student["city"] = "Shevgaon"

student.pop("course");

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

