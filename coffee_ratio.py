"""
Coffee brew ratio
"""




def determine_coffee_style(ratio):
    if ratio < 2:
        return "ristretto"
    if ratio < 3:
        return "normale"
    else:
        return "lungo"


def determine_brew_ratio(brewed_coffee, ground_coffee):
    ratio = brewed_coffee/ground_coffee
    return ratio



def check_coffee():
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo


def get_valid_number(prompt):
    number = float(input(prompt))
    return number


def main():
    ground_coffee = get_valid_number("Dose: ")
    brewed_coffee = get_valid_number("Yield: ")


    ratio = determine_brew_ratio(brewed_coffee,ground_coffee)
    style = determine_coffee_style(ratio)

    print(f"1:{ratio} is considered {style}")


# check_coffee()
main()