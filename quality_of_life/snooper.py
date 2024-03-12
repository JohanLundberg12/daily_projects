import numpy as np
import pysnooper


# pysnooper is a great debugging tool. I will print the output of the function and
# and the variables that are being used in the function.
# The output will be printed in the terminal.


@pysnooper.snoop()
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present

    return -1


arr = np.array([2, 3, 4, 10, 40])

# Function call
for x in arr:
    result = binary_search(arr, x)

    if result != -1:
        print(f"Element {x} is present at index", str(result))
    else:
        print(f"Element {x} is not present in array")
    print("-" * 50)

    print("|")
