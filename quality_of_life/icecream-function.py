from icecream import ic
import numpy as np


def a_crazy_function(crazy_input):
    a_crazy_variable = np.array([2, 3, 4, 10, 40])
    b_crazy_variable = 0
    c_crazy_variable = np.sqrt(2)

    crazy_variable = [a_crazy_variable, b_crazy_variable, c_crazy_variable]

    return crazy_variable * crazy_input


a_dic = {"Bob": [1_000_000], "Joe": {1: 2}}


class test:
    attr1 = 20
    attr2 = 30

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __repr__(self):
        return f"test({self.attr1}, {self.attr2})"

    def some_test(self):
        return self.attr1 + self.attr2


def if_else_then(a, b, c):
    ic()

    if a > b:
        ic()
    elif c > b:
        ic()
    else:
        ic()

    return a + b + c


if __name__ == "__main__":

    # we can use ic for easy inspection of variables
    ic(a_crazy_function(1))
    ic(a_crazy_function(2))
    print(ic(a_dic))
    print(ic(test.attr1))

    # ic returns its argument, so it can be used a parameter to a function
    print(a_crazy_function(ic(1)))

    # we can use ic to track which parts of the code is being executed
    print(if_else_then(1, 3, 2))
