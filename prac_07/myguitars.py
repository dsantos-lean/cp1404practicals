from prac_06.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, formatted display sorted by year."""
    guitars = []
    process_guitars_file(guitars)
    name = input("Name: ")
    while name != "":
        year = get_valid_integer("Year: ")
        cost = get_valid_float("Cost: ")
        add_guitars(cost, guitars, name, year)
        name = input("Name: ")
    guitars.sort()  # __lt__ method defined in Guitar class
    max_length = max([len(guitar.name) for guitar in guitars])
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar.name:{max_length}} ({guitar.year}), costs ${guitar.cost:>9}")
    write_to_file(guitars)


def process_guitars_file(guitars):
    """Read lines from file and save to guitars list"""
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), (parts[2]))
        guitars.append(guitar)
    in_file.close()


def get_valid_integer(prompt):
    """Get valid integer with exception based error-checking"""
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


def get_valid_float(prompt):
    """Get valid float with exception based error-checking"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Number must be >= 1")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number  # Works as intended


def add_guitars(cost, guitars, name, year):
    """Add guitar from user input to list of guitars"""
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}) $ {guitar.cost} added.")


def write_to_file(guitars):
    """Write new guitars list to csv file"""
    out_file = open("guitars.csv", "w")
    # print(guitars)
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
