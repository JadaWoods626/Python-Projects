#Parent class user
class user:
    name = "Mori"
    email = "MoriDan@outlook.com"
    password = "1234abcd$$"

def getLoginInfo(self):
    entry_name = input("Enter your name: ")
    entry_email = input("Enter youe email: ")
    entry_password = input("Enter your password: ")
    if (entry_email == self.email and entry_password == self.password):
        print("Welcome back, {}!".format(entry_name))
    else:
        print("The password or email in incorrect.")
#Child Class Employee
class Employee(user):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"
#This is the same method in the parent class "user".
#The difference is that, instead of using entry_password, we're using entry_pin.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
                print("The pin or email is incorrect")
#The following code invokes the methods inside each class for user and employee.
    customer = user()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLoginInfo()

                
