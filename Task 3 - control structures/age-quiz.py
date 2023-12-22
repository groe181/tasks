"""This program prints a statement based on the user's age"""

#The user is asked for their age and this is converted to an integer.
#The user's age is given back to them,
#combined with a statement dependant on their age.
#The else statement covers the sets of values [13, 20] and [22, 39].

#If user input cannot be converted to an integer
#or the user gives a value equal to or less than 0
#this is treated as an error and the user is asked to run the program again.


ERROR_MESSAGE = "Please run the program again and enter a number greater than or equal to 0."

try:
    AGE = int(input("How many years old are you? "))
    CONFIRMATION_MESSAGE = f"You're {AGE} years old. "

    if AGE <= 0:
        print(ERROR_MESSAGE)
    else:
        if AGE > 100:
            print(CONFIRMATION_MESSAGE + "Sorry, you're dead.")
        elif AGE >= 65:
            print(CONFIRMATION_MESSAGE + "Enjoy your retirement")
        elif AGE >= 40:
            print(CONFIRMATION_MESSAGE + "You're over the hill.")
        elif AGE == 21:
            print(CONFIRMATION_MESSAGE + "Congrats on your 21st.")
        elif AGE < 13:
            print(CONFIRMATION_MESSAGE + "You qualify for the kiddie discount")
        else:
            print(CONFIRMATION_MESSAGE + "Age is but a number")
except ValueError:
    print(ERROR_MESSAGE)
