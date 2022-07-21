"""
CP1401 2022 TR2 Assignment 1

Program 1 – Simple Interest Calculator

Student Name: <your name>

Date started: <date>

Pseudocode:
BEGIN 

PROMPT for account balance
PROMPT for time period

SET rate to 0.075

SET simple interest to balance MULTIPLY by rate MULTIPLY by time

SET future balance to balance ADD to simple interest

DISPLAY "Simple Interest Calculator"
DISPLAY "Starting balance: ", starting_balance"
DISPLAY "Time period", time_period"
DISPLAY "Based on ", time_period, "time periods at ",
          rate MULTIPLY 100, "% per period"
DISPLAY "Total interest, total interet"
DISPLAY "Future balance, future balance"


END


Expected Output:

Simple Interest Calculator
Starting balance: 10000
    Time period: 5
Based on 5 time periods at 7.5% per period
Total interest = $ 3750.00
Future balance = $ 13750.00

"""

# Calculate simple interest


def simple_interest(balance, rate, time):
    si = balance * rate * time
    return si

# Calculate future balance


def future_balance(balance, si):
    fb = balance + si
    return fb

# format output and display


def print_output(starting_balance, time_period, rate, total_interest, future_balance):
    print("Simple Interest Calculator")
    print("Starting balance: ", starting_balance)
    print("\tTime period", time_period)
    print("Based on ", time_period, "time periods at ",
          rate * 100, "% per period")
    print("Total interest = $", "{:.2f}".format(total_interest))
    print("Future balance = $", "{:.2f}".format(future_balance))


# prompt user for account balance
account_balance = int(input("Provide your account balance: "))

# prompt user for time period
time_period = int(input("Provide the time period: "))

# define interest
rate = 0.075

si = simple_interest(account_balance, rate, time_period)
fb = future_balance(account_balance, si)
print_output(account_balance, time_period, rate, si, fb)
