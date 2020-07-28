class Bank:

    __file_path = "bank.csv"
    __data = {} # to store all the bank information

    def __init__(self):
        Bank.__read_data()
        self.record = None # to store specific record

    @classmethod
    def __read_data(cls):
        try:
            file = open(Bank.__file_path, 'r')
            for line in file:
                column = line.split(';')
                Bank.__data[column[0].rstrip('\n')] = [
                    str(column[1]), 
                    str(column[2]),
                    str(column[3]),
                    float(column[4]),
                    float(column[5])
                ]
            file.close()
        except IOError:
            print('Error opening file. ' + Bank.__file_path)

    def login(self, account_number, password):
        # if the account number exist then retrieve the
        # record
        if Bank.__data.get(account_number):
            # set the current record for validation
            self.record = Bank.__data.get(account_number)

            if self.record[2] == password:
                # call welcome method
                self.info()

            else:
                # wrong password, set to None 
                self.record = None
                print("User name or Password is incorrect")

        else:
            print("Account not found")

    def info(self):
        print("=== Customer Info ===")
        print("First name ", self.record[0])
        print("Last name ", self.record[1])
        print("Checking $", self.record[3])
        print("Savings $", self.record[4])


class Customer(Bank):
    def __init__(self):
        Bank.__init__(self)

    def new_account(self):
        self.record[2]= int(input("Enter the account no : "))
        self.record[0] = input("Enter the account holder's first name : ")
        self.record[1] = input("Enter the account holder's last name : ")
        self.record[3] = int(input("Enter the type of account to deposit to checking : "))
        self.record[4] = int(input("Enter the type of account to deposit to savings :"))

        print("\n\n\nAccount Created")

    def balance(self):
        print(f"Checking balance is {self.record[3]} and Savings balance is {self.record[4]}")

    def withdraw_from_checking(self):
        amount = float(input("Enter amount to be withdrawn from checking:"))
        if self.record[3] >= amount:
            new_balance1 = self.record[3] - amount
            print(f"{amount} withdrawn from checking account. Total checking balance is {new_balance1}")
        else:
            print("Insufficient balance.")

    def withdraw_from_savings(self):
        amount = float(input("Enter amount to be withdrawn from savings:"))
        if self.record[4] >= amount:
            new_balance2 = self.record[4] - amount
            print(f"{amount} withdrawn from savings account. Total savings balance is {new_balance2}")
        else:
            print("Insufficient balance.")

    def  deposit_to_checking(self):
        amount = float(input("Enter amount to be deposited into checking:"))
        new_balance3 = self.record[3] + amount
        print(f"{amount} deposited into checking account. Total checking balance is {new_balance3}")

    def deposit_to_savings(self):
        amount = float(input("Enter amount to be deposited into savings:"))
        new_balance4 = self.record[4] + amount
        print(f"{amount} deposited into savings account. Total savings balance is {new_balance4}")

    # def transfer_money(self, account_number, other_account):
    #     pass




customer = Customer()
customer.login("10003", "uYWE732g4ga1")
print('Hello what would you like to do?')

while True:
    banker_options = ("\n1 - View Balance \t 2 - Withdraw from Savings \t 3 - Withdraw from Checking \t 4 - Deposit to Savings \t 5 - Deposit to Checking \t 6 - Create New account \t 7 - Exit")
    print(banker_options)

    selection = int(input("\nEnter your selection: "))

    # View balance
    if selection == 1:
        print(customer.balance())

        while True: 
            anything_else_question = input("Is there anything else you would like to do? yes/no: ")
            print(anything_else_question)
            if anything_else_question == "yes":
                break
            elif anything_else_question == "no":
                print("Transation is now complete.")
                print("Thanks for choosing ACME Bank.")
                exit()
            else:
                print("Invalid option")


    # Withdraw from savings
    elif selection == 2:
        print(customer.withdraw_from_savings())
        while True: 
            anything_else_question = input("Is there anything else you would like to do? yes/no: ")
            print(anything_else_question)
            if anything_else_question == "yes":
                break
            elif anything_else_question == "no":
                print("Transation is now complete.")
                print("Thanks for choosing ACME Bank.")
                exit()
            else:
                print("Invalid option")

    # Withdraw from Checking
    elif selection == 3:
        print(customer.withdraw_from_checking())
        while True: 
            anything_else_question = input("Is there anything else you would like to do? yes/no: ")
            print(anything_else_question)
            if anything_else_question == "yes":
                break
            elif anything_else_question == "no":
                print("Transation is now complete.")
                print("Thanks for choosing ACME Bank.")
                exit()
            else:
                print("Invalid option")

    # Deposit to Savings
    elif selection == 4:
        print(customer.deposit_to_savings())
        while True: 
            anything_else_question = input("Is there anything else you would like to do? yes/no: ")
            print(anything_else_question)
            if anything_else_question == "yes":
                break
            elif anything_else_question == "no":
                print("Transation is now complete.")
                print("Thanks for choosing ACME Bank.")
                exit()
            else:
                print("Invalid option")

    # Deposit to Checking
    elif selection == 5:
        print(customer.deposit_to_checking())
        while True: 
            anything_else_question = input("Is there anything else you would like to do? yes/no: ")
            print(anything_else_question)
            if anything_else_question == "yes":
                break
            elif anything_else_question == "no":
                print("Transation is now complete.")
                print("Thanks for choosing ACME Bank.")
                exit()
            else:
                print("Invalid option")

    elif selection == 6:
        print(customer.new_account())
        while True: 
            anything_else_question = input("Is there anything else you would like to do? yes/no: ")
            print(anything_else_question)
            if anything_else_question == "yes":
                break
            elif anything_else_question == "no":
                print("Transation is now complete.")
                print("Thanks for choosing ACME Bank.")
                exit()
            else:
                print("Invalid option")

    elif selection == 7:
        print("Transation is now complete.")
        print("Thanks for choosing ACME Bank.")
        exit()

    else: 
        print("That's an invalid choice.")