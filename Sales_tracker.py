"""
CP1401 2022 TR2 Assignment 1

Program 1 – Sales tracker

Student Name: <your name>

Date started: <date>

Pseudocode:

BEGIN

SET sales to []

PROMPT for number of days

WHILE number of days is less than or equal to 0
    DISPLAY "Error. Number of days must be >= 1"
    PROMPT for number of days

ELSE
    FOR day in RANGE number of days
        DISPLAY "Day ", day ADD 1, "sales? "
        PROMPT for sale
        APPEND sale to sales array

    SET total sales to 0
    FOR sale in RANGE sales
        SET total sales to total sales ADDED to sale
    
    SET average sales to total sales DIVIDED by the length of sales array
    DISPLAY "Sales Tracker"
    DISPLAY "Number of days: ", number of days
    FOR day in RANGE number of days
        DISPLAY "Day ", day, " sales: ", sales[day]
    DISPLAY "Total sales: ", "{:.2f}".format(total_sales), "for ", number_of_days,
          "days. Average sales: $", "{:.2f}".format(avg_sales), " per day."


END

Expected Output:

Sales Tracker
Number of days: -1
Error. Number of days must be >= 1
Number of days: 0
Error. Number of days must be >= 1
Number of days: 3
Day 1 sales: -2
Error. Sales must be >= 0
Day 1 sales: -3.2
Error. Sales must be >= 0
Day 1 sales: 0
Day 2 sales: 5.6
Day 3 sales: 12.82
Total sales: $18.42 for 3 days. Average sales: $6.14 per day.
Great finish!

Sales Tracker
Number of days: 2
Day 1 sales: 902.54
Day 2 sales: 801
Total sales: $1703.54 for 2 days. Average sales: $851.77 per day.
Don't slow down next time.
Sales Tracker

Number of days: 3
Day 1 sales: 9
Day 2 sales: 9
Day 3 sales: 9
Total sales: $27.00 for 3 days. Average sales: $9.00 per day.
Great finish!

"""

# format output and print

def print_output(number_of_days, sales, total_sales, avg_sales):
    print("Sales Tracker")
    print("Number of days: ",number_of_days)
    for day in range(number_of_days):
        print("Day ", day, " sales: ", sales[day])
    print("Total sales: ", "{:.2f}".format(total_sales), "for ", number_of_days,
          "days. Average sales: $", "{:.2f}".format(avg_sales), " per day.")

# calculate the total sales

def calculate_total_sales(sales):

    total_sales = 0

    for sale in sales:
        total_sales = total_sales + sale

    return total_sales

# calculate average sales

def calculate_average_sales(sales):
    total_sales = calculate_total_sales(sales)
    average_sales = total_sales/len(sales)

    return average_sales

# store all sales in this array

sales = []

# prompt for number of days
number_of_days = int(input("Enter the number of days? "))


# check if number of days is less than 0
while number_of_days <= 0:
    print("Error. Number of days must be >= 1")
    number_of_days = int(input("Enter the number of days? "))

else:

    # loop through number of day and query for sales
    for day in range(number_of_days):
        print("Day ", day + 1, "sales? ")
        sale = int(input())
        sales.append(sale)

    total_sales = calculate_total_sales(sales)
    average_sales = calculate_average_sales(sales)

    print_output(number_of_days, sales, total_sales, average_sales)
