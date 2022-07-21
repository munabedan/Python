"""
Jcu Grades
"""

from random import randint


def determine_grade(result):
    if result < 0:
        exit()
    elif result < 50:
        return "F"
    elif result < 65:
        return "P"
    elif result < 75:
        return "C"
    elif result < 85:
        return "D"
    else:
        return "HD"

def check_determine_grade():
    print(f"A result of 49 gets a grade F :",determine_grade(49))
    print(f"A result of 50 gets a grade P :",determine_grade(50))
    print(f"A result of 65 gets a grade C :",determine_grade(65))
    print(f"A result of 75 gets a grade D :",determine_grade(75))
    print(f"A result of 85 gets a grade HD :",determine_grade(85))


def main():
    result = float(input("Score: "))
    print(f"The score {result} is ",determine_grade(result))

def generate_random_results():
    number_of_results = int(input("How many random scores: "))
    
    for i in range(number_of_results):
        result = randint(1,100)
        print(f"{result} = ",determine_grade(result))

generate_random_results()
# main()
# check_determine_grade()