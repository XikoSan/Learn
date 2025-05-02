from staff_logic import load_staff, add_staff, delete_staff, edit_staff, list_staff, search_staff
    

def run():
    staff = load_staff()

    try:
        staff = add_staff(staff, name="John Doe", age=30, city="New York")
        print("Staff added successfully.")
    except ValueError as e:
        print("Error adding staff:", e)

    try:
        staff = delete_staff(staff, name="John Doe")
        print("Staff deleted successfully.")
    except ValueError as e:
        print("Error deleting staff:", e)

    try:
        staff = edit_staff(staff, name="John Doe", age=31, city="Los Angeles")
        print("Staff edited successfully.")
    except ValueError as e:
        print("Error editing staff:", e)

    staff_display = list_staff(staff)
    print("\nStaff List:")
    for person in staff_display:
        print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

    try:
        search_results = search_staff(staff, search_type="name", search_value="John Doe")
        print("\nSearch Results:")
        for person in search_results:
            print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
    except ValueError as e:
        print("Error searching staff:", e)
    
if __name__ == "__main__":
    run()
