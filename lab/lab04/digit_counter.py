def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0

    while num > 0:
        if func(num):
            counter += 1
        num = num // 10
    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    print(digit_counter(is_even, 11324499592))
