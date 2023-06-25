class MyAtm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.account = ""
        self.balance=0
        self.overview()

    def overview(self):
        entered_pin = input("enter your pin here:")
        while True:
            if entered_pin == self.pin:
                print("select one of the options above.")
                user_input = input("""
                1.to choose ur lang.
                2.to deposit.
                3.to balance inquiry.
                4.to change pin(select this option if you're a new user).
                5.to cancel
                """)
                if overview == "1":
                    if self.withdraw():
                        pass
                    else:
                        break
                elif overview == "2":
                    if self.deposit():
                        pass
                    else:
                        break
                elif overview == "3":
                    print("your balance is {}.".format(self.balance))
                    break
                elif overview == "4":
                    if self.change_pin():
                        pass
                    else:
                        break
                else:
                    break
            else:
                print("you entered incorrect password!")
                break

    def withdraw(self):
        while True:
            print("NOTE: Please enter amount divisible by 500.")
            amount_limit = 10000
            amount = int(input("enter your amount here."))
            if amount < self.balance:
                if amount_limit > amount and amount % 500 == 0:
                    self.balance -= amount
                    # return number of denomination
                    break
                else:
                    print("{} is not divisible by 500.".format(amount))
                    break
            else:
                print("there is no sufficient balance.")
                break

    def deposit(self):
        while True:
            print("deposit money on your account number.")
            get_account = input("enter your account number.")
            if get_account == self.account:
                print("""please put your money on the box.
                accepts only denomination of 500.
                """)
                denomination = int(input("enter denomination"))
                number_of_notes = int(input("enter number of your deno:"))
                if denomination == self.denomination:
                    self.balance += denomination * number_of_notes
                    print("successfully deposited {}.".format(denomination * number_of_notes))
                    break
                else:
                    break
            else:
                break

    def change_pin(self):
        while True:
            new_pin = input("enter your new pin.")
            confirm_pin = input("confirm your new pin")
            if new_pin == confirm_pin:
                print("""your pin successfully changed. make sure not to forget this pin and not to share this pin
                with anyone.""")
                self.pin = new_pin
                break
            else:
                continue


hello = MyAtm("1234", 15000, 23456789)
