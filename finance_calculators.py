# ======Capstone Project I======

# Program that allows the user to access two different financial calculators: an investment calculator and home loan repayment calculator.

# The 'import math' function is used to harness the mathematical operations needed in this program.
import math

print("Welcome to Capstone Financial Services. \n")

print("\tinvestment - to calculate the amount of interest you'll earn on your investment")
print("\tbond       - to calculate the amount of interest you'll have to pay on a home loan \n")

# The user is asked to enter their choice from the menu above. Their choice is stored into the variable 'user_input.'
# The 'lower()' method has been used to accept user input in UPPER case, lower case, or mIxEd case. 
user_input = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower() 

# An 'if' statment is used to generate an error message if user does not type in a valid input. The code will not proceed unless a valid choice is made. 
if user_input not in ("investment", "bond"):
    print("\nInvalid option. Enter either 'investment' or 'bond' from the menu above to proceed.")  

# Nested 'elif-if-elif' statment is executed if the 'investment' option is selected. The user is prompted to type the prinicipal amount, 
# interest rate, term, and if they want 'simple' or 'compound' interest, which are then stored into variables. Within this 'elif' 
# code block is an 'if' statement to calculate 'simple interest' and a elif statement to calculate 'compound interest.' The result of
# the calculations are output to the user. 
elif user_input == "investment":
    print("\n\tInvestment Interest Calculator: \n")
    P = float(input("\tEnter the principal amount: "))
    R = float(input("\tEnter the rate of interest: "))
    T = int(input("\tEnter the number of years you plan to invest: "))
    interest = str(input("\tDo you want 'simple' or 'compound' interest?: ")).lower() # 'lower()' method used to accept any case entry.

    if interest == "simple":
        simple_interest = (P * T * R)/100 + P # Formula to calculate 'simple interest.'
        print(f"\n\tAfter {T} years, at an interest rate of {R}% per annum, the total amount you will receive is £",round(simple_interest, 2))
        print("\nThank you for using the Investment Interest Calculator at Capstone Financial Services. \n") 
        # 'round() method used to round up the float decimal places by 2. Makes its easier to read when output. 
    
    elif interest == "compound":
        compound_interest = P * (math.pow((1 + R/100), T)) # Formula to calculate 'compound interest.'
        print(f"\n\tAfter {T} years, at an interest rate of {R}% per annum, the total amount you will receive is £",round(compound_interest, 2))
        print("\nThank you for using the Investment Interest Calculator at Capstone Financial Services. \n")

# 'Elif' code block will run if 'bond' option selected. The user enters the data that is needed for the calculation and the input is stored as a variable. 
# The calculation is then performed using the variables and the output shows the monthly repayment. 
elif user_input == "bond":
    print("\n\tBond Repayment Calculator: \n")
    P = float(input("\tEnter the present value of the house: "))
    I = float(input("\tEnter the rate of interest: "))
    N = int(input("\tEnter the number of months you plan to take to repay the bond: "))

    i = I/100 # The interest rate entered by the user is divided by 100.
 
    repayment = (i/12) * (1/(1-(1+i/12)**(-N)))*P # Formula to calculate 'monthly repayment.'
    print(f"\n\tYou will have to pay £{round(repayment, 2)} every month.") 
    print("\nThank you for using the Bond Repayment Calculator at Capstone Financial Services.\n")
    