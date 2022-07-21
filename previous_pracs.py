"""
Calculate salary
"""


def determine_worker_salary(level):
    if level < 1:
        print("Invalid worker level")
        exit()

    elif level >= 10:
        print("Invalid worker level")
        exit()

    else:
        return level * 5000


def main():
    worker_level = int(input("Worker level: "))
    salary = determine_worker_salary(worker_level)
    print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")


main()


"""
Print grid(rows, columns)
"""


def print_numbers(columns, rows):

    for row in range(rows):
        for column in range(columns):
            print(column, end=" ")
        print("\n")


def main():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    print_numbers(columns, rows)


main()
