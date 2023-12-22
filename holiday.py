"""This program calculates a user's total holiday cost based on their plane, hotel and car-rental costs."""

class Flight:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

flights = [
    Flight('New York', 500),
    Flight('Washington DC', 600),
    Flight('Boston', 400),
    Flight('Miami', 700),
    Flight('Los Angles', 1000)
]

def hotel_cost(nights):
    price = 100
    return nights * price

def plane_cost(city):
    return flights[city].price

def car_rental_cost(days):
    price = 50
    return days * price

def holiday_cost(nights, city, days):
    return hotel_cost(nights) + plane_cost(city) + car_rental_cost(days) 

city_options = ""
for index, flight in enumerate(flights):
    city_options += f"{index + 1} --- {flight.destination} --- £{flight.price}\n"

city_flight = int(input("What city are you flying to?" + "\n" + city_options)) - 1
num_nights = int(input("How many nights will you be staying at a hotel? "))                 
rental_days = int(input("How many days will you hire a car for? "))


print(f"Hotel cost: £{holiday_cost(num_nights, city_flight, rental_days)}")
