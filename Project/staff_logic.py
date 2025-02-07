import json

DATA_FILE = "staff.json"

def load_staff():

    try:
        with open(DATA_FILE, "r") as file:
            staff = json.load(file)
            print("Staff data loaded successfully.")
    except (json.JSONDecodeError, FileNotFoundError):
        print("No existing staff data found. Creating a new list.")
        staff = []
    return staff
    

def save_staff(staff):
    with open(DATA_FILE, "w") as file:
        json.dump(staff, file, indent=4)
    print("Staff data saved successfully.")

def add_staff(staff):
    input_name = input("Enter a name of the staff member: ")
    while any(person["name"].lower() == input_name.lower() for person in staff):
        print("This name already exists. Try another.")
        input_name = input("Enter a name of the staff member: ")
    
    input_age_str = input("Enter an age: ")
    while not input_age_str.isdigit() or int(input_age_str) < 0:
        print("Invalid age.")
        input_age_str = input("Enter an age: ")
    input_age = int(input_age_str)

    input_city = input("Enter a city: ")

    staff.append({"name": input_name, "age": input_age, "city": input_city})
    save_staff(staff)
    print(f"Staff member {input_name} added successfully.")
    return staff

def delete_staff(staff):
    name_to_delete = input("Enter a name of the staff member to delete: ")

    for i, person in enumerate(staff):
        if person["name"].lower() == name_to_delete.lower():
            del staff[i]
            save_staff(staff)
            print(f"Staff member {name_to_delete} deleted successfully.")
            return staff
    print(f"Staff member {name_to_delete} not found.")
    return staff

def edit_staff(staff):
    name_to_edit = input("Enter a name of the staff member to edit: ")
    found = False
    for person in staff:
        if person["name"].lower() == name_to_edit.lower():
            found = True
            print(f"Staff member {name_to_edit} found.")

            new_name = input(f"Enter a new name for {name_to_edit} (leave blank to not change): ")
            if new_name and any(person["name"].lower() == new_name.lower() for person in staff):
                print("This name already exists. Try another.")
                new_name = input(f"Enter a new name for {name_to_edit} (leave blank to not change): ")
            else:
                person["name"] = new_name
                print(f"Name updated to {new_name}.")

            new_age_str = input(f"Enter a new age for {name_to_edit} (leave blank to not change): ")
            if new_age_str:
                while not new_age_str.isdigit() or int(new_age_str) < 0:
                    print("Invalid age.")
                    new_age_str = input(f"Enter a new age for {name_to_edit} (leave blank to not change): ")
                person["age"] = int(new_age_str)

            new_city = input(f"Enter a new city for {name_to_edit} (leave blank to not change): ")
            if new_city:
                person["city"] = new_city
            save_staff(staff)
            break

    if not found:
        print(f"Staff member {name_to_edit} not found.")
    return staff

def search_staff(staff_list, search_type, search_value):
    """
    Поиск сотрудника по заданному критерию
    """
    results = []
    for staff_member in staff_list:
        if staff_member.get(search_type) == search_value:
            results.append(staff_member)
    
    if not results:
        raise ValueError(f"No staff found with {search_type}: {search_value}")
    
    return results

def list_staff(staff):
    if not staff:
        print("No staff members available.")
    else:
        print("Staff List:")
        for person in staff:
            print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")