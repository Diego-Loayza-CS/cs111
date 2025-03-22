from pair import Pair, nil
from operator import add, sub, mul, truediv


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    # Write your code here
    expression = expression.replace('(', '( ')
    expression = expression.replace(')', ' )')
    return expression.split()


def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    if tokens[index] == "(":

        operator = tokens[index + 1]

        if index != 0:
            pair_list, index = parse_tokens(tokens, index + 2)
            operator = Pair(operator, pair_list)
        elif index == 0:
            index += 2

        new_list, index = parse_tokens(tokens, index)
        return Pair(operator, new_list), index

    elif tokens[index] == ")":
        return nil, index + 1

    else:
        try:
            if "." in tokens[index]:
                num = float(tokens[index])
            else:
                num = int(tokens[index])

            new_list, index = parse_tokens(tokens, index + 1)
            return Pair(num, new_list), index

        except:
            raise TypeError


def parse(tokens):
    token_list, index = parse_tokens(tokens, 0)
    return token_list


def reduce(func, operands, initial):
    if operands.rest is nil:
        return func(initial, operands.first)
    else:
        initial = func(initial, operands.first)
        return reduce(func, operands.rest, initial)


def apply(operator, operands):
    if operator == '+':
        return reduce(add, operands, 0)
    elif operator == '*':
        return reduce(mul, operands, 1)
    elif operator == '/':
        return reduce(truediv, operands.rest, operands.first)
    elif operator == '-':
        return reduce(sub, operands.rest, operands.first)
    else:
        raise TypeError('invalid')


def eval_loop(pair):
    if pair.rest is nil:
        return Pair(eval(pair.first), nil)
    else:
        return Pair(eval(pair.first), eval_loop(pair.rest))





def eval(syntax_tree):
    if isinstance(syntax_tree, int) or isinstance(syntax_tree, float):
        return syntax_tree
    elif isinstance(syntax_tree, Pair):
        operator = syntax_tree.first
        pair = syntax_tree.rest

        pair = eval_loop(pair)
        return apply(operator, pair)
    else:
        raise TypeError


if __name__ == '__main__':

    print("Welcome to the CS 111 Calculator Interpreter.")

    while True:
        response = input("calc >> ")
        if response == "exit":
            break

        try:
            parsed = parse(tokenize(response))
            print(eval(parsed))

        except:
            print("wrong input hermano")
            continue
    print("Goodbye!")
