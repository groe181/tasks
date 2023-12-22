"""
Finance calculator that determines investment returns using simple or compound interest, 
as well as monthly repayments for bonds.
"""
import math

#readme
#handle inputs that are not int or negative numbers
#test using other calculators
#descriptions of output
#round up figures
#float int

print("\nInvestment - to calculate the amount of interest you'll earn on your investment"
      +"\nBond - to calculate the amount you'll have to pay on a home loan"
      +"\n\nEither enter 'investment' or 'bond' from the menu above to proceed")

CALCULATOR_SELECTION = input().lower()

if CALCULATOR_SELECTION == "investment":
    DEPOSIT = float(input("What is your deposit? "))
    YEARLY_INTEREST_RATE = float(input("What is the interest rate? ")) / 100
    YEARS_INVESTING = int(input("How many years do you plan to invest? "))
    INTEREST = input("Do you want to calculate 'simple' or 'compound' interest? ")

    if INTEREST == "simple":
        print(DEPOSIT * (1 + YEARLY_INTEREST_RATE * YEARS_INVESTING))
    elif INTEREST == 'compound':
        print(DEPOSIT * math.pow((1 + YEARLY_INTEREST_RATE), YEARS_INVESTING))
    else:
        print("Invalid input. Please enter either 'simple' or 'compund'.")

elif CALCULATOR_SELECTION == "bond":
    HOUSE_VALUE = int(input("What is the present value of your house? "))
    MONTHLY_INTEREST_RATE = (int(input("What is the yearly interest rate? ")) / 100) / 12
    REPAYMENT_MONTHS = int(input("How many months do you plan to repay the bond over? "))

    print((MONTHLY_INTEREST_RATE * HOUSE_VALUE)
          / (1 - (1 + MONTHLY_INTEREST_RATE)**(-REPAYMENT_MONTHS))
          )

else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")
