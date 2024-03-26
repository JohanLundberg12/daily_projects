import sys



# walrus in an if statement
def check_is_single_digit(number):
    if is_single_digit:= len(list(str(number))) == 1:
        print(f"{number} is a single digit: {is_single_digit}")
    else:
        print(f"{number} is not a single digit: {is_single_digit}")


# walrus to assign result of operation in a foor loop or if statement
def squared_walrus_for_loop(number):
    for i in range(0, y:= number**2):
        print(y)


def number_modulo_2(number):
    return number % 2


# Use walrus operator in a list comprehension
def list_comp_with_walrus(number):
    y = int(number) ** 2
    modulo = [True if (v := number_modulo_2(i)) == 0 else "not zero" for i in range(0, y)]

    return modulo


if __name__ == "__main__":
    number = int(sys.argv[1])

    check_is_single_digit(number)

    squared_walrus_for_loop(number)

    print(list_comp_with_walrus(number))



    
