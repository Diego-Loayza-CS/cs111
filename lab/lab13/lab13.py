def filter(lst, cond):
    """Returns a list where each element is an element where `cond(elem)` returns `True`.
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> is_even = lambda x : x % 2 == 0 # Even numbers have remainder 0 when divided by 2.
    >>> filter(nums, is_even)
    [2, 4, 6, 8, 10]
    """
    modified_list = []
    for elem in lst:
        if cond(elem):
            modified_list.append(elem)
    return modified_list


def print_cond(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> print_cond(5)(is_even)
    2
    4
    """

    def func(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return func


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """

    def function(n):
        i = 1
        count = 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count

    return function


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """

    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)

    return inner_print


# OPTIONAL QUESTION
#####################

def make_repeater(func, n):
    """Return the function that computes the nth application of func.
    >>> increment = lambda x: x+1
    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> triple = lambda x: x*3
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> square = lambda x: x**2
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def operation(x):
        i = 1
        num = x
        while i <= n:
            num = func(num)
            i += 1
        return num

    return operation