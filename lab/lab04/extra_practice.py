def largest_factor(n):
    biggest_factor = 0
    i = 1

    if n == 1:
        biggest_factor = i
    else:
        while i < n:
            if n % i == 0:
                biggest_factor = i
            i += 1

    return biggest_factor


def missing_digits(n):
    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        if last_digit != second_to_last_digit:
            diff = last_digit - second_to_last_digit
            counter += diff - 1
        n //= 10

    return counter
