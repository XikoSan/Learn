import json

staff = [{"name": "Harry", "age": 20, "city": "London"},
         {"name": "Leny", "age": 17, "city": "New York"},
         {"name": "Genry", "age": 32, "city": "Santafe"}]

try:
    with open("staff.json", "r") as file:
        staff = json.load(file)
except json.JSONDecodeError:
    staff = []


input_name = input("Enter a name: ")
while any(person["name"] == input_name for person in staff):
    print("This name already exists. Try another.")
    input_name = input("Enter a name: ")

input_age_str = input("Enter an age: ")
while not input_age_str.isdigit() or int(input_age_str) < 0:
    print("Invalid age.")
    input_age_str = input("Enter an age: ")
input_age = int(input_age_str)

input_city = input("Enter a city: ")


staff.append({"name": input_name, "age": input_age, "city": input_city})

with open("staff.json", "w") as file:
    json.dump(staff, file, indent=4)

print(f"Staff member {input_name} added successfully.")
