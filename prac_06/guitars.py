from prac_06.guitar import Guitar


def main():
    """Add and display guitars program, using Guitar class"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":  # Keep adding
        year = get_valid_number("Year: ")
        cost = float(get_valid_number("Cost: "))
        add_guitars(cost, guitars, name, year)
        name = input("Name: ")
    display_guitars(guitars)


def add_guitars(cost, guitars, name, year):
    """Add guitar from user input to list of guitars"""
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")


def get_valid_number(prompt):
    """Get valid number with exception based error-checking"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be >= 1")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number  # Works as intended


def display_guitars(guitars):
    """Display list of guitar names, years, cost and if they are vintage"""
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))  # Test data
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))  # Test data
    max_guitar_length = max([len(guitar.name) for guitar in guitars])
    for i, guitar in enumerate(guitars, 1):
        guitar.get_age()
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(
            f"Guitar {i}: {guitar.name:>{max_guitar_length}} ({guitar.year}), worth $ {guitar.cost:>10,.2f}{vintage_string}")


main()
