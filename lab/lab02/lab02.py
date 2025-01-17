def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    new_list = []
    i = 0
    while i < len(s):
        new_list.append(s[i] * i)
        i += 2
    return new_list


def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    i = 0
    final_list = []
    while i < len(s):
        new_list = []
        new_list.extend([s[i], t[i]])
        final_list.append(new_list)
        i += 1
    return final_list


def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    i = 0
    with open("text.txt") as input_file:
        with open("output.txt", "w") as output_file:
            list_lines = input_file.readlines()
            while i < len(list_lines):
                output_file.write(f"{i + 1}: {list_lines[i]}")
                i += 1


########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    i = 1
    while i < n:
        if n % i == 0:
            all_factors.append(i)
        i += 1
    return all_factors
