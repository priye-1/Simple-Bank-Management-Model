"""   A Bank Mangement Program   """
import random
import sys


class User():
    """This class is to register and store user details"""

    # class attribute
    BankName = "Reimnet Bank"

    # instance attributes
    def __init__(self, name, phone_no, location):
        self.name = name
        self.phone_no = phone_no
        self.location = location

    # instance methods  
    def user_details(self):
        """This function is to get user details and display them"""
        print("\n------------------------------")
        print("Welcome to REIMNET BANK! \nFill in Details to start process ")
        print("------------------------------")
        self.name = input("\nKindly enter your full name: ")
        self.phone_no = int(input("Enter phone no: "))
        self.location = input("Enter your location: ")

        # to display User Details
        print("\nBANK DETAILS: ")
        return"Name: {} \nPhone Number: {} \nLocation: {}".format(self.name, self.phone_no, self.location,)


class Account_Register(User):
    """ This class is to register and store bank details"""

    # instance attributes
    def __init__(self, name, phone_no, location, acct_no,  account_type):
        super(Account_Register, self).__init__(name, phone_no, location)
        self.acct_no = acct_no
        self.account_type = account_type

    def acct_details(self):
        """this function is to get account details and store them"""

        print("\nhello " + self.name + "! proceed to account registration")
        choice0 = ""
        no_of_accts = 0

        # while loop to continually run this part of the programme till user exits it
        while choice0 != "break":

            # generating random number
            self.acct_no = random.sample(range(1, 10), 6)

            # converting the list of random numbers to a string
            str_acct_no = ''.join(map(str, self.acct_no))

            print("\n----------------------------")
            print("Number of current accounts = " + str(no_of_accts))
            print("------------------------------")

            # Getting the user desired type of account
            self.account_type = input(
                "\nType of account? (savings/current): \nenter (a) for savings(b) for current and enter (break) to end: ")

            # conditional statements to perform different operations as desired by user
            if self.account_type == "a":
                print("\ncongrats " + self.name + "with account number 1140" + str_acct_no +
                      " you have created a new savings account with Reimnet bank!")
                account_balance = 0
                choice2 = ""

                # while loop to continually run operations chosen by the user until the user exits
                while choice2 != "d":
                    print("\n------------------------------------------------------------------")
                    choice = input(
                        "Want to deposit, withdraw, create another account or end programme? \n(a) to deposit \n(b) to withdraw \n(c) to add account \n(d) to end programme: ")
                    print("-------------------------------------------------------------------")

                    if choice == "a":
                        amount = int(
                            input("\nHow much do you want to deposit? "))
                        # increments account balance by amount deposited by the user and prints new balance
                        account_balance += amount
                        print("new account balance = N" + str(account_balance))

                        print("\n-----------------------------------------------------------------")
                        choice2 = input(
                            "To go back to menu enter(menu) or enter (d) to end programme: ")
                        print("-------------------------------------------------------------------")

                        # exits programme as desired by user
                        if choice2 == "d":
                            sys.exit()

                    elif choice == "b":
                        amount = int(
                            input("\nHow much do you want to withdraw? "))

                        # conditional statements to check if withdrawal is possible or not, prints its balance if it is
                        if amount < account_balance:
                            account_balance -= amount
                            print("You have deducted N" + str(amount) +
                                  " new account balance = N" + str(account_balance))

                            print("\n-------------------------------------------------------------------")
                            choice2 = input(
                                "To go back to menu enter (menu) or enter (d) to end programme: ")
                            print("-------------------------------------------------------------------")

                            # exits programme as desired by user
                            if choice2 == "d":
                                sys.exit()

                        elif amount > account_balance:
                            print("Insufficient funds!")
                            print("\n-------------------------------------------------------------------")
                            choice2 = input(
                                "To go back to menu enter(menu) or enter (d) to end programme:")
                            print("-------------------------------------------------------------------")

                            # exits programme as desired by user
                            if choice2 == "d":
                                sys.exit()

                        else:
                            # decrements account balance by the amount  by user and prints balance
                            account_balance -= amount
                            print("You have deducted " + str(amount) +
                                  " new account balance = N" + str(account_balance))

                            print("\n-------------------------------------------------------------------")
                            choice2 = input(
                                "To go back to menu enter(menu) or enter (d) to end programme:")
                            print("-------------------------------------------------------------------")

                            # exits programme as desired user
                            if choice2 == "d":
                                sys.exit()


                    elif choice == "c":
                        break

                    elif choice == "d":
                        sys.exit()

                    no_of_accts += 1

                
            elif self.account_type == "b":
                print("wna check this stuff")

            elif self.account_type == "break":
                break

            else:
                print("Kindly enter (0) or (1) for savings or current")
                # acct_details(self)

            print("\n-------------------------------------------------------------------------------------------------------------------------------------------")
            dict = {"Name": self.name, "Phone-Number": self.phone_no, "Location": self.location, "Account-Number": str_acct_no,"Account-Type": self.account_type}
            print(dict)
            print("------------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    user1 = User("", 0, "")
    user2 = Account_Register("", 0, "", 0, "")
    print(user1.user_details())
    print(user2.acct_details())
    
