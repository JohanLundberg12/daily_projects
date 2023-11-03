# we can add the asterisk * to the function parameter
# to accept an arbitrary number of arguments
def multiply(*numbers):
    result = 1
    for n in numbers:
        result = result * n
    return result


print(multiply(1, 2, 3))


# we can collect any extra arguments into a tuple using *args
def function(a, b, *args):
    print(a, b)
    print(args)


function(1, 2, 3, 4, 5)


# *args picks up any unnamed extra arguments
# **kwargs picks up any named extra arguments
def function2(a, b, *args, keyword=True, **kwargs):
    print(a, b)
    print(args)
    print(keyword)
    print(kwargs)


function2(1, 2, 3, 4, 5, keyword=False, key1="value", key2=999)


# example that will not work
# this is because, python is having a hard time figuring
# out whether a=1, b=2 should go into **kwargs as keyword arguments
# or into a, b arguments
print("This will not work: function(a=1, b=2, 5, 3, 4, param=42)")


# **variale unpacks our dict into keyword arguments for the function
d = {"param_a": 43, "param_b": 44}
function2(1, 2, 5, 3, 4, param=42, **d)
function2(1, 2, *[5, 3, 4], param=42, **d)

import json
import pathlib


def dict_to_config(dictionary, file="config.json", verbose=False, **kwargs):
    """
    dictionary
    file
    verbose
    kwargs - passed to json.dumps
    """

    json_txt = json.dumps(dictionary, **kwargs)
    if verbose:
        print(json_txt)
    pathlib.Path(file).write_text(json_txt)


dict_to_config({"a": 1, "b": 2}, verbose=True, indent=4)
