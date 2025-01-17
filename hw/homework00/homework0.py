## CONSTANTS SHOULD GO BELOW THIS COMMENT ##
PI = 3.14159265

PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1

DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12

LARGE_PRICE = 14.68
MEDIUM_PRICE = 11.48
SMALL_PRICE = 7.28


def print_amounts(large_pizzas, medium_pizzas, small_pizzas):
    print(
        f"{large_pizzas} large pizzas, {medium_pizzas} medium pizzas, and {small_pizzas} small pizzas will be needed.")


def print_inches(total_square_inches, individual_square_inches):
    print(f"""
A total of {total_square_inches:.2f} square inches of pizza will be ordered ({individual_square_inches:.2f} per guest).""")


def main():
    ## YOUR CODE SHOULD GO IN THIS FUNCTION ##
    guests = int(input("Please enter how many guests to order for:"))

    # Define pizza characteristics
    large_pizzas = guests // PEOPLE_PER_LARGE
    medium_pizzas = (guests % PEOPLE_PER_LARGE) // PEOPLE_PER_MEDIUM
    small_pizzas = ((guests % PEOPLE_PER_LARGE) % PEOPLE_PER_MEDIUM) // PEOPLE_PER_SMALL
    if ((guests % PEOPLE_PER_LARGE) % PEOPLE_PER_MEDIUM) % PEOPLE_PER_SMALL != 0:
        small_pizzas = small_pizzas + 1

    total_square_inches = PI * (
            (large_pizzas * (DIAMETER_LARGE / 2) ** 2) + (medium_pizzas * (DIAMETER_MEDIUM / 2) ** 2) + (
            small_pizzas * (DIAMETER_SMALL / 2) ** 2))

    individual_square_inches = total_square_inches / guests

    # Print order details
    print_amounts(large_pizzas, medium_pizzas, small_pizzas)
    print_inches(total_square_inches, individual_square_inches)

    # Financial details
    tip = int(input("Please enter the tip as a percentage (i.e. 10 means 10%):")) / 100
    base_cost = (large_pizzas * LARGE_PRICE) + (medium_pizzas * MEDIUM_PRICE) + (small_pizzas * SMALL_PRICE)
    final_cost = base_cost * (1 + tip)
    print(f"The total cost of the event will be: ${final_cost:.2f}.")


if __name__ == "__main__":
    main()
