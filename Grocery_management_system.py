import mysql.connector

# connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ankansarmah@sql",
    database="grocery_management_system"
)
c = conn.cursor()

# create the tables
c.execute('''CREATE TABLE IF NOT EXISTS fruits
             (id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255),
              price FLOAT)''')
c.execute('''CREATE TABLE IF NOT EXISTS vegetables
             (id varchar(2),
              name VARCHAR(255),
              price FLOAT)''')
c.execute('''CREATE TABLE IF NOT EXISTS dairy_products
             (id varchar(2),
              name VARCHAR(255),
              price FLOAT)''')
c.execute('''CREATE TABLE IF NOT EXISTS oils
             (id varchar(2),
              name VARCHAR(255),
              price FLOAT)''')

def view_items(table_name):
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    if len(rows) == 0:
        print("No items in this category.")
        return
    print(f"{table_name.capitalize()} List:")
    for row in rows:
        print(f"{row[0]}. {row[1]}: Rs {row[2]:.2f}")

def add_item():
    item_id = input("Enter the item ID: ")
    table_names = {1: "fruits", 2: "vegetables", 3: "dairy_products", 4: "oils"}
    table_num = int(input("Choose your product (1: Fruits, 2: Vegetables, 3: Dairy Products, 4: Oils): "))
    table_name = table_names.get(table_num)
    if table_name is None:
        print("Invalid table number.")

    c.execute(f"SELECT * FROM {table_name} WHERE id=%s", (item_id,))
    row = c.fetchone()
    if row is None:
        print("Item not found.")
        return
    item_name, item_price = row[1], row[2]
    quantity = int(input("Enter the quantity: "))
    total_price = item_price * quantity
    print(f"{quantity} {item_name}(s) added to your list for a total of Rs {total_price:.2f}.")
    return total_price

items = []
total_price = 0.0

while True:
    print("\n1. View items\n2. Add item to list\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        table_names = {1: "fruits", 2: "vegetables", 3: "dairy_products", 4: "oils"}
        table_num = int(input("Choose your product (1: Fruits, 2: Vegetables, 3: Dairy Products, 4: Oils): "))
        table_name = table_names.get(table_num)
        if table_name is None:
            print("Invalid table number.")
        view_items(table_name)
    elif choice == 2:
        total_price += add_item()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")

# close the database connection
conn.close()
