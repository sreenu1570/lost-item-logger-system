import csv

# 🔹 Report Lost Item
def report_lost():
    name = input("Enter your name: ")
    item = input("Enter lost item: ")
    loc = input("Enter location: ")

    with open("lost_items.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, item, loc])

    print("Lost item recorded successfully!")

# 🔹 Report Found Item
def report_found():
    name = input("Enter your name: ")
    item = input("Enter found item: ")
    loc = input("Enter location: ")

    with open("found_items.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, item, loc])

    print("Found item recorded successfully!")

# 🔹 View Lost Items
def view_lost():
    print("\n--- Lost Items ---")
    try:
        with open("lost_items.csv", "r") as f:
            items = list(csv.reader(f))

            if not items:
                print("No lost items found!")
                return

            for row in items:
                print(f"{row[0]} lost {row[1]} at {row[2]}")

    except FileNotFoundError:
        print("No lost items found!")

# 🔹 View Found Items
def view_found():
    print("\n--- Found Items ---")
    try:
        with open("found_items.csv", "r") as f:
            items = list(csv.reader(f))

            if not items:
                print("No found items!")
                return

            for row in items:
                print(f"{row[0]} found {row[1]} at {row[2]}")

    except FileNotFoundError:
        print("No found items!")

# 🔹 Delete Lost Item
def delete_lost():
    name = input("Enter your name to delete: ")
    item = input("Enter item to delete: ")

    rows = []

    try:
        with open("lost_items.csv", "r") as f:
            for row in csv.reader(f):
                if not (row[0] == name and row[1] == item):
                    rows.append(row)

        with open("lost_items.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Record deleted successfully!")

    except FileNotFoundError:
        print("No file found!")

# 🔹 Menu
def menu():
    print("\n===== LOST ITEM LOGGER SYSTEM =====")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View Lost Items")
    print("4. View Found Items")
    print("5. Delete Lost Item")
    print("6. Exit")

# 🔹 Main Program Loop
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        report_lost()
    elif choice == '2':
        report_found()
    elif choice == '3':
        view_lost()
    elif choice == '4':
        view_found()
    elif choice == '5':
        delete_lost()
    elif choice == '6':
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Please try again.")