"""This program prints a pattern of stars."""

#Run a for loop that runs 9 times which is equal to the height of the pattern.
#with num reflecting the number of iterations that has run.
#Each time the loop runs:
#if the value of num is less than or equal to 5, print that many "*"
#otherwise subtract the number of iterations from 10,
#and print that many stars. This is to reduce the width of the pattern by 1
#each time.

for num in range(1, 10):
    if num <= 5:
        print("*" * num)
    else:
        print("*" * (10 - num))
