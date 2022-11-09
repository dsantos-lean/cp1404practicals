from prac_06.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display sorted by year."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()  # __lt__ method defined in Guitar class
    for guitar in guitars:
        print(guitar)


main()
