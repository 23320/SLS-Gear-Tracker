import sqlite3

#shows menu and gets the user to pick which option they want.
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
            break #the break will stop running the program
        else:
            print("Invalid choice")
#this will show the all the gear in the databse.
def show_gear(cursor):
    cursor.execute("SELECT * FROM gear")
    rows = cursor.fetchall()
    if not rows:
        print("No gear found in database")
    else:
        for row in rows:
            print(row)

#you will be able to add gear with this function
def add_gear(cursor, conn):
    cursor.execute("SELECT COUNT(*) FROM gear")
    if cursor.fetchone()[0] == 0:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='gear'")
    name = input("Name: ")
    gear_type = input("Type: ")
    while True:
        try:
            cost = float(input("Cost: "))
            break
        except:
            print("Invalid input")
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except:
            print("Invalid input")
        
    cursor.execute("INSERT INTO gear (name, type, cost, quantity) VALUES (?, ?, ?, ?)", (name, gear_type, cost, quantity))
    conn.commit() #conn.commit will save the changes made
    print("Gear added.")
    
#this will update the quanitity of gear   
def update_quantity(cursor, conn):
    gear_id = input("Enter gear ID to update: ")

    cursor.execute("SELECT * FROM gear WHERE id = ?", (gear_id,))
    if cursor.fetchone() is None:
        print("ID does not exist") #if the user enters a Id that dosent exsist this message come up
        return
    while True:
        try:
            new_qty = int(input("New quantity: "))
            break
        except:
            print("Invalid input") # when a non number is entered
    cursor.execute("UPDATE gear SET quantity = ? WHERE id = ?", (new_qty, gear_id))
    conn.commit()#saves the changes
    print("Quantity updated.") #once the quanity updates this message come up

# this one you will be able to delete gear with.
def delete_gear(cursor, conn):
    gear_id = input("Enter gear ID to delete: ")
    cursor.execute("SELECT * FROM gear WHERE id = ?", (gear_id,))
    if cursor.fetchone() is None:
        print("ID does not exist") # if you dont ebetr the right id to delete a item this will come up
        return
    cursor.execute("DELETE FROM gear WHERE id = ?", (gear_id,))
    conn.commit() #saves the changes
    print("Gear deleted.")#comes up when you delete the gear

#this will connect it back to the database then start the menu
with sqlite3.connect('gear.db') as conn:
    cursor = conn.cursor()
    menu(cursor, conn)