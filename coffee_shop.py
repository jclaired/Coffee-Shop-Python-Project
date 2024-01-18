# Coffe shop employees:
# Clerks -> Set order, check pending orders
# Delivery -> update an order as completed
# Manager -> View reports and statistics

# Importing CSV files
import csv

file = open("orders.txt", "a")
order = []

# Users credentials
users = {}
users['Justine'] = {'role': 'clerks', 'password': '2222'}
users['Claire'] = {'role': 'delivery', 'password': '2222'}
users['Desepeda'] = {'role': 'manager', 'password': '2222'}


# Login
print("Login")
username = input("Username: ")
password = input("Password: ")

# Check if user is ok
valid = False
role = None
if username in users:
    if users[username]['password'] == password:
        valid = True
        role = users[username]['role']

if valid: 
    while True:
        if role == 'clerks':
            # Clerks roles/duties
            print("1. Set orders")
            print("2. Check pending orders")
            print("0. Exit")
            choice = input("Choose: ")

            id_count = 0

            if choice == '1':
                file.write("order_id,customer_name,address,description,date,total_amount\n")
                orders = {}
                while True:
                    customer_name = input("Enter name of customer: ")
                    if customer_name == '-':
                        break
                    else:
                        order_id = id_count + 1
                        orders[order_id] = {
                            'customer_name': customer_name,
                            'address': input("Enter address of the customer: "),
                            'description': input("Enter description: "),
                            'date': input("Enter Date (YYYY-MM-DD): "),
                            'total_amount': input("Enter total amount of order: ")
                        }

                        # Write each order to the file with its ID
                        file = open('orders.txt', 'a')
                        order_details = [str(order_id), *orders[order_id].values()]
                        file.write(",".join(order_details) + '\n')
                        

                        # Increment the ID count
                        id_count += 1

                    # Check if the user wants to add another order
                    set_order_again = input("Would you like to set another order? (Yes/No) ")

                    if set_order_again == 'No':
                        break
            elif choice == '2':
                with open('orders.txt', 'r') as file:
                    orders = file.readlines()
                # Filter orders that are not yet delivered
                filtered_orders = []
                for order in orders:
                    if "successfully delivered" not in order.strip():
                        filtered_orders.append(order.strip())

                # Display filtered order details
                for order in filtered_orders:
                    print(order)
            elif choice == '0':
                break
        elif role == 'delivery':
            # Delivery people role/duties
            print("1. Update an order")
            print("0. Exit")
            choice = input("Choose: ")
            if choice == '1':
                order_id = input("Enter order ID number: ")

                with open('orders.txt', 'r') as file:
                    orders = file.readlines()

                    # Find the order corresponding to the specified ID
                    updated_order_found = False
                    for index, order in enumerate(orders):
                        order_details = order.strip().split(',')
                        actual_order_id = order_details[0]

                        # Check if the entered order ID matches the actual order ID
                        if order_id == actual_order_id:
                            # Split the order details into a list
                            updated_order_details = order.strip().split(',')
                            updated_order_details.append('successfully delivered')
                            updated_order = ','.join(updated_order_details)

                            # Reconstruct the updated order
                            updated_order = ','.join(updated_order_details)
                            
                            orders[index] = updated_order + '\n'
                            updated_order_found = True
                            break
                    with open('orders.txt', 'w') as file:
                        file.writelines(orders)
                # Update the order details in the file only if an order was found
                if updated_order_found:
                    print("Order status updated successfully.")
                else:
                    print("Order ID not found.")
            elif choice == '0':
                break
        elif role == 'manager':
            # Managers role/duties
            print("1. View report")
            print("2. View statistics")
            print("0. Exit")
            choice = input("Choose: ")
            if choice == '1':
                print("1. Number of orders placed by one specific customer")
                print("2. Number of orders in one specific day")
                print("3. Total amount of all orders delivered")
                print("4. Total amount of the orders placed by a specifc customer")
                print("5. Total amount of the orders placed on specific day")
                print("0. Exit")
                choice2 = input("Choose: ")
                if choice2 == '1':
                    customer_name = input("Enter the customer's name: ")

                    with open('orders.txt', 'r') as file:
                        orders = file.readlines()

                        order_counts = 0
                        for order in orders:
                            order_details = order.strip().split(',')
                            order_customer_str = order_details[1].strip()
                            if order_customer_str == customer_name:
                                order_counts += 1

                        print(f"Orders placed on {customer_name}: {order_counts}")
                elif choice2 == '2':
                    order_date = input("Enter the order date (YYYY-MM-DD): ")

                    with open('orders.txt', 'r') as file:
                        orders = file.readlines()

                        order_counts = 0
                        for order in orders:
                            order_details = order.strip().split(',')
                            order_date_str = order_details[4].strip()
                            if order_date_str == order_date:
                                order_counts += 1

                        print(f"Orders placed on {order_date}: {order_counts}")
                elif choice2 == '3':
                    successful_delivered_orders = []

                    with open('orders.txt', 'r') as file:
                        orders = file.readlines()
                        total_amount = 0
                        for order in orders:
                            order_details = order.strip().split(',')
                            if 'successfully delivered' in order:
                                total_amount += int(order_details[5].strip())

                    # Display the total amount on the terminal
                    print(f"Total order amount for successfully delivered orders: ${total_amount:,.2f}")
                elif choice2 == '4':
                     # Calculate total amount of orders placed by a specific customer
                    customer_name = input("Enter the customer's name: ")

                    with open('orders.txt', 'r') as file:
                        orders = file.readlines()

                        # Initialize the total amount
                        total_amount = 0

                        # Calculate the total amount for each order by the specified customer
                        for order in orders:
                            order_details = order.strip().split(',')
                            if customer_name in order_details:
                                total_amount += int(order_details[5].strip())

                        # Display the total amount of orders placed by the specified customer
                        print(f"Total amount of orders placed by {customer_name}: ${total_amount:,.2f}")
                elif choice2 == '5':
                    date = input("Enter the order date (YYYY-MM-DD): ")

                    with open('orders.txt', 'r') as file:
                        orders = file.readlines()

                        total_amount = 0
                        for order in orders:
                            order_details = order.strip().split(',')
                            if date in order_details:
                                total_amount += int(order_details[5].strip())

                        print(f"Total amount of orders placed on {date}: ${total_amount:,.2f}")
                elif choice2 == '0':
                    break
                else:
                    input("Please enter choice again")
            elif choice == '2':
                while True:
                    print("1. Name of customers")
                    print("2. Orders Entered per user")
                    print("3. All data entered")
                    print("4. Total amount of orders per day")
                    print("0. Exit")
                    choice = input("Choose: ")
                    if choice == '1':
                        with open('customer_report.csv', 'w') as csvfile:
                            writer = csv.writer(csvfile)

                            with open('orders.txt', 'r') as file:
                                orders = file.readlines()

                                for order in orders:
                                    order_details = order.strip().split(',')
                                    customer_name = order_details[1]
                                    writer.writerow([customer_name])

                        print("Customer report generated successfully.")
                    elif choice == '2':
                        # Generate order report
                        with open('order_report.csv', 'w') as csvfile:
                            writer = csv.writer(csvfile)
                            with open('orders.txt', 'r') as file:
                                orders = file.readlines()

                                for order in orders:
                                    order_details = order.strip().split(',')
                                    writer.writerow(order_details)

                        print("Order report generated successfully.")
                    elif choice == '3':
                        # Generate all data report
                        with open('all_data_report.csv', 'w') as csvfile:
                            writer = csv.writer(csvfile)

                            with open('orders.txt', 'r') as file:
                                orders = file.readlines()
                                for order in orders:
                                    order_details = order.strip().split(',')
                                    writer.writerow(order_details)

                        print("All data report generated successfully.")
                    elif choice == '4':
                        # Generate daily order amount report
                        daily_order_amounts = {}

                        with open('order_details.txt', 'r') as file:
                            orders = file.readlines()

                            for order in orders:
                                order_details = order.strip().split(',')
                                date = order_details[4].strip()
                                total_amount = float(order_details[5].split())

                                if date not in daily_order_amounts:
                                    daily_order_amounts[order_date] = 0

                                daily_order_amounts[date] += total_amount

                        with open('daily_order_report.csv', 'w') as csvfile:
                            writer = csv.writer(csvfile)

                            for date, total_amount in daily_order_amounts.items():
                                writer.writerow([date, total_amount])

                        print("Daily order amount report generated successfully.")
                    elif choice == '0':
                        break

            elif choice == '0':
                break
                        