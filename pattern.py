"""This program prints a pattern of stars."""

#Initialise a string variable assigned to an asterisk character (representing a star).
#Run a for loop that runs 9 times, with the number of iterations performed assigned to variable num.
#Each time the loop runs:
    #print the value assigned to stars
    #change the value of stars by:
        #if the value of num is less than 5, concatenate the current value of stars with an additional "*"
        #else slice the last value of stars to remove an "*"


stars = "*"

for num in range(1, 10):
    print(stars)
    if num < 5:
        stars += "*"
    else:
        stars = stars[:-1]
        