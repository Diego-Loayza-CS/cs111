if __name__ == "__main__":
    # *** YOUR CODE HERE ***
    integer = int(input("Enter an integer divisible by 20 => "))

    if not integer % 20 == 0:
        print(f"""
{integer} is not divisible by 20!""")
    else:

        floating_point_number = float(input("Enter a floating point number => "))
        familymember = input("Enter a family relationship (mother, grandfather, cousin, etc.) => ")
        noun = input("Enter a noun => ")
        adjective = input("Enter an adjective => ")

        print(f"""
{integer // 20} score and {floating_point_number:.3f} years ago, our fore{familymember}s brought forth upon this {noun} a {adjective} nation.""")