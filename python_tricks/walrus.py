x = 5


# walrus to assign result of operation in a foor loop or if statement
for i in range(0, y := x**2):

    print(i)


if n := (len(list(str(x))) == 1):
    print(f"Length of list(str({x})) is 1")


def check_x(x):
    return x % 2


# Use walrus operator in a list comprehension
y = x**2
modulo = [True if (v := check_x(i)) == 0 else "not zero" for i in range(0, y)]

print(modulo)
