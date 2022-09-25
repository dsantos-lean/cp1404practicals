"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temperature = get_temperature()
            result = convert_celsius_to_fahrenheit(temperature)
            print("Result: {:.2f} F".format(result))
        elif choice == "F":
            temperature = get_temperature()
            result = convert_fahrenheit_to_celsius(temperature)
            print("Result: {:.2f} C".format(result))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_temperature():
    temperature = float(input("Enter temperature: "))
    return temperature


def convert_celsius_to_fahrenheit(temperature):
    return temperature * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(temperature):
    return 5 / 9 * (temperature - 32)


main()
