"""A program to determine the award an entrant of a traithlon should receive."""

#Define functions for requesting and validating user input.
#Explain how the program works to the user.
#Request a time from the user for each leg.
#If user input is invalid, recursively request valid inputs.
#Calculate the user's total traithlon time and present it back to them.
#Determine the award the user should receive.
#Present the resulting award back to the user.

def request_entry(leg):
    """Ask user for the time of a specific traithlon leg"""
    return validate_entry(input(f"{leg} time: "), leg)

def validate_entry(leg_time, leg):
    """
    Convert input to an integer and check value is greater than or equal to 0.
    If value is invalid, recursively request entry again.
    """
    try:
        converted_time = int(leg_time)
        if converted_time >= 0:
            return converted_time
        print("Please enter a number greater than 0")
        return request_entry(leg)
    except ValueError:
        print("Please enter a number")
        return request_entry(leg)


#Statements presented to the user to introduce the program.
print("Welcome to the Award Calculator to determine your prize")
print("Please enter the time in minutes it took you to complete each leg of your triathlon")

#Request times from the user of each leg.
SWIMMING_TIME = request_entry("Swimming")
RUNNING_TIME = request_entry("Running")
CYCLING_TIME = request_entry("Cycling")

#Calculate the user's total traithlon time and present it back to them.
TOTAL_TIME = SWIMMING_TIME + RUNNING_TIME + CYCLING_TIME
print(f"Your total time was: {TOTAL_TIME} minutes.")

#Determine the award the user should receive.
#Present the resulting award back to the user.
if TOTAL_TIME >= 111:
    print("Unfortunately you haven't won an award.")
elif TOTAL_TIME >= 106:
    print("You have won the Provincial Scroll.")
elif TOTAL_TIME >= 101:
    print("You are awarded Provincial Half Colours.")
elif TOTAL_TIME >= 0:
    print ("You are awarded the Provincial Colours.")


#Notes to reviewer:
#I could have used the 'and' operator, specifing the exact time range for each award,
#as outlined below.
#This solution could be easier to read, however requires more operations so is less efficient.
#The order of the conditions could be adjusted based on the liklehood an entrant will win award.
#If more people are likely to meet the qualifying time,
#it will be more efficient to put this condition first, as the rest of the code won't run.
#I haven't included an else statement as a number provided by the user is below 0
#is dealt with in the 'validate_entry' function.

"""
if TOTAL_TIME >= 111:
    print("Unfortunately you haven't won an award.")
elif TOTAL_TIME >= 106 and TOTAL_TIME <=110:
    print("You have won the Provincial Scroll.")
elif TOTAL_TIME >= 101 and TOTAL_TIME <=105:
    print("You are awarded Provincial Half Colours.")
elif TOTAL_TIME >= 0 and TOTAL_TIME <=100:
    print ("You are awarded the Provincial Colours.")
"""
