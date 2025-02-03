from operator import add, mul


# Write your code here for Q1
def product(n):
    value = 1
    if type(n) != int or n < 1:
        raise ValueError
    for x in range(1, n + 1):
        value *= x
    return value


def summation(n):
    value = 0
    if type(n) != int or n < 0:
        raise ValueError
    for x in range(1, n + 1):
        value += x
    return value


#############################################
# Q2

square = lambda x: x * x

sqrt = lambda x: x ** 0.5  # x^0.5 == √x


def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers)
    # `sorted` returns a sorted list. `sorted` works. 
    if len(numbers) % 2 == 0:
        right_mid = (len(numbers) // 2)
        left_mid = right_mid - 1
        print(left_mid)
        print(right_mid)
        return mean([numbers[left_mid], numbers[right_mid]])
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[running_high_num] = 0
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

        if counts[num] > counts[running_high_num]:
            running_high_num = num

    return running_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers:
        total_dist += square(num - avg)

    return sqrt(total_dist / len(numbers))


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    info = {}
    info["mean"] = mean(numbers)
    info["median"] = median(numbers)
    info["mode"] = mode(numbers)
    info["std_dev"] = std_dev(numbers)
    return info


#############################################
# (OPTIONAL) Write your code here for Accumulate, Invert, and Change
def factored(n, value, operation):
    if type(n) != int or n < 0:
        raise ValueError
    for x in range(1, n + 1):
        value = operation(value, x)
    return value


def product_short(n):
    return factored(n, 1, mul)


def summation_short(n):
    return factored(n, 0, add)


def accumulate(merger, initial, n):
    if n < initial or type(n) != int:
        raise ValueError
    if merger == add:
        return merger(initial, summation_short(n))
    elif merger == mul:
        return merger(initial, product_short(n))


def invert(x, limit):
    if x == 0:
        raise ZeroDivisionError
    if 1 / x < limit:
        return 1 / x
    else:
        return limit


def change(x, y, limit):
    if x == 0:
        raise ZeroDivisionError
    if abs(y - x) / x < limit:
        return abs(y - x) / x
    else:
        return limit


def refactored(condition, limit, x):
    if x == 0:
        raise ZeroDivisionError
    if condition < limit:
        return condition
    else:
        return limit


def invert_short(x, limit):
    return refactored(1 / x, limit, x)


def change_short(x, y, limit):
    return refactored(abs(y - x) / x, limit, x)
