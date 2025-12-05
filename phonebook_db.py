import sqlite3

def create_database():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            Name TEXT PRIMARY KEY,
            Phone TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_entry():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Entries (Name, Phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Entry added!")
    except sqlite3.IntegrityError:
        print("That name already exists in the phonebook.")

    conn.close()


def look_up():
    name = input("Enter name to search: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
    result = cur.fetchone()

    if result:
        print(f"{name}'s phone number is: {result[0]}")
    else:
        print("Name not found.")

    conn.close()

def update_entry():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute("UPDATE Entries SET Phone = ? WHERE Name = ?", (new_phone, name))
    conn.commit()

    if cur.rowcount > 0:
        print("Phone number updated.")
    else:
        print("Name not found.")

    conn.close()

def delete_entry():
    name = input("Enter name to delete: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    conn.commit()

    if cur.rowcount > 0:
        print("Entry deleted.")
    else:
        print("Name not found.")

    conn.close()

def show_all():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM Entries")
    rows = cur.fetchall()

    if rows:
        print("\n--- Phonebook Entries ---")
        for row in rows:
            print(f"Name: {row[0]} | Phone: {row[1]}")
    else:
        print("Phonebook is empty.")

    conn.close()

def main():
    create_database()

    while True:
        print("\n=== PHONEBOOK MENU ===")
        print("1. Add Entry")
        print("2. Look Up Phone Number")
        print("3. Update Phone Number")
        print("4. Delete Entry")
        print("5. Show All Entries")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            look_up()
        elif choice == "3":
            update_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            show_all()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# running the program
if __name__ == "__main__":
    main()
