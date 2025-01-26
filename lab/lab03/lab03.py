def average_temperature(temps):
    """
    Given a list of temperatures, TEMPS, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """
    average = sum(temps) / len(temps)
    return round(average, 2)


def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """
    average = round(sum(temps) / len(temps), 2)
    i = 0
    for temp in temps:
        difference = temp - average
        if difference > 5:
            i += 1
    print(f"There were {i} day(s) more than 5 degrees above the average of {round(average, 1)}.")
    return i


def is_palindrome(word):
    """
    Given a single word, WORD, determine if it is a palindrome or not.
    Print a message that includes the word stating it is or is not a
    palindrome and return True if it is and False otherwise
    >>> is_palindrome('rotator')
    rotator is a palindrome.
    True
    >>> is_palindrome('apple')
    apple is not a palindrome.
    False
    """
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
    return word == reversed_word


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    even_list = s[::2]
    multiplied_list = []
    i = 0
    while i < len(even_list):
        multiplied_item = even_list[i] * (i * 2)
        multiplied_list.append(multiplied_item)
        i += 1
    return multiplied_list
