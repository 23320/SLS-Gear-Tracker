import sqlite3


def menu(cursor, conn):
    while True:
        print("\nSurf Life Saving Gear Tracker")
        print("1. Show gear")
        print("2. Add gear")
        print("3. Update gear quantity")
        print("4. Delete gear")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_gear(cursor)
        elif choice == "2":
            add_gear(cursor, conn)
        elif choice == "3":
            update_quantity(cursor, conn)
        elif choice == "4":
            delete_gear(cursor, conn)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def show_gear(cursor):
    cursor.execute("SELECT * FROM gear")
    rows = cursor.fetchall()
    if not rows:
        print("Database is empty.")
    else:
        for row in rows:
            print(row)


def add_gear(cursor, conn):
    cursor.execute("SELECT COUNT(*) FROM gear")
    if cursor.fetchone()[0] == 0:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='gear'")

    
    name = input("Name: ")
    gear_type = input("Type: ")
    try:
        cost = float(input("Cost: "))
        quantity = int(input("Quantity: "))
    except:
        print("Invalid input")
        return

    cursor.execute("INSERT INTO gear (name, type, cost, quantity) VALUES (?, ?, ?, ?)", (name, gear_type, cost, quantity))
    conn.commit()
    print("Gear added.")
    
    
def update_quantity(cursor, conn):
    gear_id = input("Enter gear ID to update: ")
    new_qty = input("New quantity: ")
    cursor.execute("UPDATE gear SET quantity = ? WHERE id = ?", (new_qty, gear_id))
    conn.commit()
    print("Quantity updated.")


def delete_gear(cursor, conn):
    gear_id = input("Enter gear ID to delete: ")
    cursor.execute("DELETE FROM gear WHERE id = ?", (gear_id,))
    conn.commit()
    print("Gear deleted.")


with sqlite3.connect('gear.db') as conn:
    cursor = conn.cursor()
    menu(cursor, conn)