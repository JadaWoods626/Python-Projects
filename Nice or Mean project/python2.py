def start():
    print(get_number())


def get_number():
    number = 12
    return number




if __name__ == "__main__":
    start()


def start():
    print("hello {}!".format(get_name()))


def get_name():
    name = input("What is your name? ")
    return name



if __name__ == "__main__":
    start()


def start():
    f_name = "Jada"
    l_name = "woods"
    age = 22
    gender = "female"
    get_info(f_name,l_name,age,gender)


def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} and I am a {}.".format(f_name,l_name,age,gender))


if __name__ == "__main__":
    start()
