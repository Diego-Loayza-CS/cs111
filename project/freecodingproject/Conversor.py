def welcome():
    print()
    print("Welcome to the Unit Converter!")


def categories():
    print()
    category = input("""To close the program at any point, press '9'.
    
Available Categories:
1. Temperature
2. Distance
3. Weight
4. Time

Choose a Category (1-4): """)
    return check_input(category, 4, categories)


def check_input(num, limit, function):
    try:
        number = int(num)
        if number in range(1, limit + 1) or number == 9:
            return number
        else:
            print()
            print(f"That number is out of range! Pick a number from 1-{limit}, or press '9' to exit the program.")
            print()
            return function()
    except ValueError:
        print()
        print(f"Invalid format! Pick a number from 1-{limit}, or press '9' to exit the program.")
        print()
        return function()


def run_category():
    print()

    if selection == 1:
        print("""Available units in Temperature:
1. Celsius
2. Fahrenheit
3. Kelvin""")

    elif selection == 2:
        print("""Available units in Distance:
1. Meters
2. Kilometers
3. Miles
4. Feet""")

    elif selection == 3:
        print("""Available units in Weight:
1. Kilograms
2. Grams
3. Pounds
4. Ounces""")

    elif selection == 4:
        print("""Available units in Time:
1. Seconds
2. Minutes
3. Hours
4. Days""")

    else:
        print("Unknown Error")

    print()


def source_unit():
    source = input(f"Select the Source Unit (1-{lim}): ")
    return check_input(source, lim, get_initial)


def get_lim():
    if selection == 1:
        return 3
    else:
        return 4


def get_initial():
    run_category()
    return source_unit()


def desired_unit():
    desired = input(f"Select the Desired Unit (1-{lim}): ")
    return check_input(desired, lim, get_target)


def get_target():
    return desired_unit()


def check_different():
    if initial == target:
        print()
        print("You can't convert to the same unit!")
        print()
        return False
    return True


def temperature():
    if initial == 1:
        if target == 2:
            return value * (9 / 5) + 32
        if target == 3:
            return value + 273.15

    if initial == 2:
        if target == 1:
            return (value - 32) * (5 / 9)
        if target == 3:
            return (value - 32) * (5 / 9) + 273.15

    if initial == 3:
        if target == 1:
            return value - 273.15
        if target == 2:
            return (value - 273.15) * (9 / 5) + 32


def distance():
    if initial == 1:
        if target == 2:
            return value / 1000
        if target == 3:
            return value / 1609.344
        if target == 4:
            return value * 3.280839895

    if initial == 2:
        if target == 1:
            return value * 1000
        if target == 3:
            return value / 1.609344
        if target == 4:
            return value * 3280.839895

    if initial == 3:
        if target == 1:
            return value * 1609.344
        if target == 2:
            return value * 1.609344
        if target == 4:
            return value * 5280

    if initial == 4:
        if target == 1:
            return value / 3.280839895
        if target == 2:
            return value / 3280.839895
        if target == 3:
            return value / 5280


def weight():
    if initial == 1:
        if target == 2:
            return value * 1000
        if target == 3:
            return value * 2.2046226218
        if target == 4:
            return value * 35.27396195

    if initial == 2:
        if target == 1:
            return value / 1000
        if target == 3:
            return value * 0.0022046226218
        if target == 4:
            return value * 0.0352739619

    if initial == 3:
        if target == 1:
            return value * 0.45359237
        if target == 2:
            return value * 453.59237
        if target == 4:
            return value * 16

    if initial == 4:
        if target == 1:
            return value * 0.0283495231
        if target == 2:
            return value * 28.349523125
        if target == 3:
            return value / 16


def time():
    if initial == 1:
        if target == 2:
            return value / 60
        if target == 3:
            return value / 3600
        if target == 4:
            return value / 86400

    if initial == 2:
        if target == 1:
            return value * 60
        if target == 3:
            return value / 60
        if target == 4:
            return value / 1440

    if initial == 3:
        if target == 1:
            return value * 3600
        if target == 2:
            return value * 60
        if target == 4:
            return value / 24

    if initial == 4:
        if target == 1:
            return value * 86400
        if target == 2:
            return value * 1440
        if target == 3:
            return value * 24


def convert():
    if selection == 1:
        converted = temperature()
    elif selection == 2:
        converted = distance()
    elif selection == 3:
        converted = weight()
    elif selection == 4:
        converted = time()
    else:
        converted = "Unknown Error"

    print()
    print(f"{value} {unit1} are equivalent to {converted:.2f} {unit2}.")


def yes_or_no(string, function):
    if string == "yes":
        return True
    elif string == "no":
        return False
    else:
        print()
        print("Invalid input! Please write 'yes' or 'no'")
        return function()


def repeat():
    print()
    decision = input("Do you want to convert again? (yes/no): ")
    print()
    return yes_or_no(decision, repeat)


def get_quantity():
    print()
    quantity = input("Enter the amount to convert: ")
    try:
        number = float(quantity)
        return number
    except ValueError:
        print()
        print(f"Invalid format! Enter a valid number")
        print()
        return get_quantity()


def get_name(item):
    if selection == 1:
        if item == 1:
            return "Celsius"
        if item == 2:
            return "Fahrenheit"
        if item == 3:
            return "Kelvin"

    if selection == 2:
        if item == 1:
            return "Meters"
        if item == 2:
            return "Kilometers"
        if item == 3:
            return "Miles"
        if item == 4:
            return "Feet"

    if selection == 3:
        if item == 1:
            return "Kilograms"
        if item == 2:
            return "Grams"
        if item == 3:
            return "Pounds"
        if item == 4:
            return "Ounces"

    if selection == 4:
        if item == 1:
            return "Seconds"
        if item == 2:
            return "Minutes"
        if item == 3:
            return "Hours"
        if item == 4:
            return "Days"


def show_conversion():
    print()
    print(f"You selected the conversion: {unit1} → {unit2}.")


def verify_conversion():
    print()
    decision = input("""Is this conversion correct?
Type 'yes' to proceed, or 'no' to select another category: """)
    return yes_or_no(decision, verify_conversion)


if __name__ == '__main__':
    welcome()
    while True:
        selection = categories()
        if selection == 9:
            break
        lim = get_lim()
        initial = get_initial()
        if initial == 9:
            break
        target = get_target()
        if target == 9:
            break
        if check_different():
            unit1 = get_name(initial)
            unit2 = get_name(target)
            show_conversion()
            if verify_conversion():
                value = get_quantity()
                convert()
                if not repeat():
                    break
    print()
    print("See you next time!")
