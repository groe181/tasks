#This example program is meant to demonstrate errors.
 
#There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program\n") #Syntax error, caused by missing parentheses. 
#Removed additional print function and added new line to string above to increase efficiency

#Variables declaring the user's age, casting the str to an int, and printing the result
age = 24 #
age_str = f"{age} years old" #Logical error. This string won't cast to an int and is unnecessary as line 11 creates the same string. 
print(f"I'm" + {age} + "years old.") 

# Variables declaring additional years and printing the total years of age
years_from_now = 3 #Logical error. Should be an integer.
total_years = age + years_from_now

print(f"The total number of years: {total_years}") #age_years is not a variable.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"

#HINT, 330 months is the correct answer

