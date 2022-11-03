def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = separate_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/N) ").upper()
        if choice != "" or choice != "Y":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def separate_name_from_email(email):
    names = email.split('@')[0]
    parts = names.split('.')
    names = " ".join(parts).title()
    return names


main()