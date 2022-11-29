from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi(name="Bentley", fuel=200, fanciness=2)
my_taxi.drive(18)
print(my_taxi)
print(f"Total fare is ${my_taxi.get_fare():.2f}")
