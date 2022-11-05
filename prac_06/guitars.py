from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    """Test data"""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    max_guitar_length = max([len(guitar.name) for guitar in guitars])
    for i, guitar in enumerate(guitars, 1):
        # print(guitar)
        guitar.get_age()
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(
            f"Guitar {i}: {guitar.name:>{max_guitar_length}} ({guitar.year}), worth $ {guitar.cost:>10,.2f}{vintage_string}")


main()
