#Write a program to demonstrate the bank management Console based application 

class Banker:
    def add_customer(self, customers, customer_id, name, balance, opening_date):
        customers[customer_id] = {'name': name, 'balance': balance, 'Opening Date': opening_date}

    def view_customer(self, customers, customer_id):
        if customer_id in customers:
            return customers[customer_id]
        else:
            return None

    def search_customer(self, customers, name):
        for customer_id, details in customers.items():
            if details['name'] == name:
                return customer_id, details
        return None, None

    def view_all_customers(self, customers):
        return customers

    def total_amount_in_bank(self, customers):
        total = sum(details['balance'] for details in customers.values())
        return total

    def update_customer(self, customers, customer_id, name, balance):
        if customer_id in customers:
            customers[customer_id]['name'] = name
            customers[customer_id]['balance'] = balance
            return True
        else:
            return False


class Customer:
    def withdraw(self, balance, amount):
        if balance >= amount:
            balance -= amount
            return balance, True
        else:
            return balance, False

    def deposit(self, balance, amount):
        balance += amount
        return balance


def banker_menu(banker):
    customers = {}
    
    while True:
        print("\nWelcome to banker's App\nOperations Menu")
        print("1)Add Customer")
        print("2)View Customer")
        print("3)Search Customer")
        print("4)View All Customer")
        print("5)Total Amount In Bank")
        print("6)Update Customer")
        print("7)Exit")

        banker_choice = input("Enter your choice: ")

        if banker_choice == "1":
            customer_id = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            balance = float(input("Enter Opening Balance: "))
            opening_date = input("Enter Opening Date: ")
            banker.add_customer(customers, customer_id, name, balance, opening_date)
            print("Customer added successfully.")
        elif banker_choice == "2":
            customer_id = input("Enter Customer ID: ")
            customer_details = banker.view_customer(customers, customer_id)
            if customer_details:
                print("Customer Details:", customer_details)
            else:
                print("Customer not found.")
        elif banker_choice == "3":
            name = input("Enter Customer Name: ")
            customer_id, customer_details = banker.search_customer(customers, name)
            if customer_id:
                print(f"Customer with ID {customer_id} found:", customer_details)
            else:
                print("Customer not found.")
        elif banker_choice == "4":
            all_customers = banker.view_all_customers(customers)
            print("All Customers:", all_customers)
        elif banker_choice == "5":
            total_amount = banker.total_amount_in_bank(customers)
            print("Total Amount in Bank:", total_amount)
        elif banker_choice == "6":
            customer_id = input("Enter Customer ID to update: ")
            name = input("Enter updated Customer Name: ")
            balance = float(input("Enter updated Balance: "))
            if banker.update_customer(customers, customer_id, name, balance):
                print("Customer details updated successfully.")
            else:
                print("Customer not found.")
        elif banker_choice == "7":
            print("Exiting banker's menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def customer_menu(banker):
    customers = {}
    
    while True:
        print("\nWelcome to customer's App\nOperations Menu")
        print("1)Withdraw Amount")
        print("2)Deposit Amount")
        print("3)View Balance")
        print("4)Exit")

        customer_choice = input("Enter your choice: ")

        if customer_choice == "1":
            customer_id = input("Enter Customer ID: ")
            customer_details = banker.view_customer(customers, customer_id)
            if customer_details:
                customer = Customer()
                customer.balance = customer_details['balance']
                amount = float(input("Enter Amount to Withdraw: "))
                customer.balance, success = customer.withdraw(customer.balance, amount)
                if success:
                    print("Amount withdrawn successfully.")
                else:
                    print("Insufficient balance.")
            else:
                print("Customer not found.")
        elif customer_choice == "2":
            customer_id = input("Enter Customer ID: ")
            customer_details = banker.view_customer(customers, customer_id)
            if customer_details:
                customer = Customer()
                customer.balance = customer_details['balance']
                amount = float(input("Enter Amount to Deposit: "))
                customer.balance = customer.deposit(customer.balance, amount)
                print("Amount deposited successfully.")
            else:
                print("Customer not found.")
        elif customer_choice == "3":
            customer_id = input("Enter Customer ID: ")
            customer_details = banker.view_customer(customers, customer_id)
            if customer_details:
                print("Current Balance:", customer_details['balance'])
            else:
                print("Customer not found.")
        elif customer_choice == "4":
            print("Exiting customer's menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


banker = Banker()

while True:
    print("WELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
    print("SELECT YOUR ROLE")
    print("1)BANKER")
    print("2)CUSTOMER")
    print("3)EXIT")

    role_choice = input("Enter your choice: ")

    if role_choice == "1":
        banker_menu(banker)
    elif role_choice == "2":
        customer_menu(banker)
    elif role_choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
