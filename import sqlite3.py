import sqlite3

# Connect to or create the database
conn = sqlite3.connect('gear.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS gear (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    cost REAL,
    quantity INTEGER
)
''')
conn.commit()

# Show menu
def menu():
    while True:
        print("\nSurf Life Saving Gear Tracker")
        print("1. Show gear")
        print("2. Add gear")
        print("3. Update gear quantity")
        print("4. Delete gear")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_gear()
        elif choice == "2":
            add_gear()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            delete_gear()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

# View gear
def show_gear():
    cursor.execute("SELECT * FROM gear")
    for row in cursor.fetchall():
        print(row)

# Add gear
def add_gear():
    name = input("Name: ")
    gear_type = input("Type: ")
    cost = float(input("Cost: "))
    quantity = int(input("Quantity: "))
    cursor.execute("INSERT INTO gear (name, type, cost, quantity) VALUES (?, ?, ?, ?)", (name, gear_type, cost, quantity))
    conn.commit()
    print("Gear added.")

# Update quantity
def update_quantity():
    gear_id = input("Enter gear ID to update: ")
    new_qty = input("New quantity: ")
    cursor.execute("UPDATE gear SET quantity = ? WHERE id = ?", (new_qty, gear_id))
    conn.commit()
    print("Quantity updated.")

# Delete gear
def delete_gear():
    gear_id = input("Enter gear ID to delete: ")
    cursor.execute("DELETE FROM gear WHERE id = ?", (gear_id,))
    conn.commit()
    print("Gear deleted.")

# Run the menu
menu()

# Close connection when done
conn.close()