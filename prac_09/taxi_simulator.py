from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
from car import Car

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                try:
                    current_taxi = taxis[taxi_choice]
                except IndexError:
                    print("Invalid taxi choice")
            except ValueError:
                print("Taxi choice must be a number")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = int(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_fare:.2f}")
                total_bill += trip_fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
