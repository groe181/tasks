"""
This program calculates a user's total holiday cost based on their plane, 
hotel and car-rental costs.
"""

#Define a class for flight information, including destination and price.
#Instantiate flight information and store in a list.
#Define functions for calculating hotel, plane, and car rental costs.
#Define a function that adds these costs together to give a total holiday cost.
#Produce a description of the flight options to show to the user,
#including destination, price and an easy way to select their option,
#by choosing a number.
#Request from the user their chosen flight (by selecting an option),
#how many nights they will stay in a hotel,
#and how many days they will rent a  car.
#Inform the user of the total cost of their holiday.


class Flight:
    """A class to represent a flight containing where the flight goes to 
    and the price of the plane ticket."""
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
    """Returns the product of the price per night
    and the number of nights in the hotel."""
    price = 100
    return nights * price

def plane_cost(city):
    """Retrives the price for flying to the chosen city 
    based on the order the flight dictionary appears in the 'flights list."""
    return flights[city].price

def car_rental_cost(days):
    """Returns the product of the car rental per day
    and the number of days the car is rented for."""
    price = 50
    return days * price

def holiday_cost(nights, city, days):
    "Sums up the component parts of the holiday cost provided by the user."
    return hotel_cost(nights) + plane_cost(city) + car_rental_cost(days) 

#Produces a string that shows the user the flight options by looping through
#the 'flights' list.
#This is used in an input function, which value is assigned to 'city_flight'
#further below.
#A seperate string is produced for each flight and these are concatenated
#with each flight sitting on a new line.
#Each flight has a number based on the index position of the flight in the
#'flights' list plus 1, to not confuse the user with starting from 0.
#The values for each flight's destination and price are accessed from the
#flight's dictionary.
city_options = ""
for index, flight in enumerate(flights):
    city_options += f"{index + 1} --- {flight.destination} --- £{flight.price}\n"

#Request information from the user, convert given values to integers and
#assign values to appropriate variables.
#N.B. 1 is subtracted from the value given for flight destination so that the
#correct index value is passed to the 'plane_cost' function.
city_flight = int(input("What city are you flying to?" + "\n" + city_options)) - 1
num_nights = int(input("How many nights will you be staying at a hotel? "))             
rental_days = int(input("How many days will you hire a car for? "))

#Present the total holiday cost back to the user.
print(f"Hotel cost: £{holiday_cost(num_nights, city_flight, rental_days)}")
