from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 5421.50)


def run_tests():
    """Test different age and vintage status outputs"""
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print("{} get_age() - Expected 9. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


run_tests()

