class User:
    name = 'No Name Provided'
    email = ' '
    passwoord = '1234abcd'
    account_number = 0

class Employees(User):
    base_pay = 20.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
