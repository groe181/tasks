"""This program calculates the average of a set of numbers entered by the user."""

#Initialise variables for the latest number the user provides, the total, and the number of entries.
#Explain the program to the user.
#Continually request that the user enters a number, until the number given is -1.
#If the input cannot be converted to a number, request the user enters a number,
#without assigning new values to the variables.
#If the input is valid:
    #assign a new value for the current number given
    #add this to the total.
    #increase the number of entries by 1.
#Once -1 has been entered, remove this from the total and the number of entries.
#If only -1 has been entered, handle the error caused by dividing by 0.
#Compute the average and provide this to the user.

current = None
entries = 0
total = 0

print("Please enter the numbers you would like to calculate the average of."
      +"\nTo conclude the program, enter '-1'. "
      +"This final entry will not been included in the average.\n")

while current != -1:
    #add 1 to entries in the string below, because entries is updated after user input.
    current = input(f"Entry {entries + 1}: ")
    try:
        current = float(current)
        total += current
        entries += 1
    except ValueError:
        print("The entry above is invalid and has not been included. Please enter a number.")
        continue

try:
    #remove the -1 entered by the user from total and entries to get the correct average.
    average = (total + 1) / (entries - 1)
    print(f"\nThe average of the numbers entered is: {average}")
except ZeroDivisionError:
    print("\nPlease run the program again and enter at least one number.")
