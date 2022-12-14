PASSWORD_LENGTH = 10


def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) != PASSWORD_LENGTH:
        print("Invalid length")
        password = input("Enter password: ")
    return password


main()
