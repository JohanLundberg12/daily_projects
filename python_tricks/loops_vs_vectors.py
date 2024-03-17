"Comparing the speed of for loops vs vectors in Python"

import time

import numpy as np
import pandas as pd


def _print_stars(n):
    print("*" * n)


# comparing the speed of for loops vs vectors in Python


def for_loop_sum_vs_vector_sum(n):
    start = time.time()

    total = 0

    for item in range(0, n):
        total = total + item

    end = time.time()

    print("Time taken for for loop:", end - start)

    start = time.time()

    total = np.sum(np.arange(0, n))

    end = time.time()
    print("Time taken for vector sum:", end - start)


for_loop_sum_vs_vector_sum(100000)
print("Sub conclusion: Vectors are faster than for loops in Python")
_print_stars(50)

# mathematical operations on dataframes to change values of cells by constant
#  comparison of for loops vs vectors


def for_loop_change_vs_vector_change(n):
    df = pd.DataFrame(
        np.random.randint(0, 50, size=(n, 4)), columns=["A", "B", "C", "D"]
    )

    start = time.time()

    for idx, row in df.iterrows():
        df.at[idx, "calculation"] = row["A"] + row["B"] + row["C"]

    end = time.time()

    print("Time taken for for loop:", end - start)

    start = time.time()
    df["calculation"] = df["A"] + df["B"] + df["C"]
    end = time.time()
    print("Time taken for vector change:", end - start)


for_loop_change_vs_vector_change(1000)
print("Sub conclusion: Vectors are faster than for loops in Python")
_print_stars(50)


# comparison of if else statements with loops and vectors


def if_else_vs_vector_comparison(n):
    df = pd.DataFrame(
        np.random.randint(0, 50, size=(n, 4)), columns=["A", "B", "C", "D"]
    )

    start = time.time()

    for idx, row in df.iterrows():
        if row["A"] > 25:
            df.at[idx, "calculation"] = row["A"] + row["B"] + row["C"]
        else:
            df.at[idx, "calculation"] = row["A"] - row["B"] - row["C"]

    end = time.time()

    print("Time taken for for loop:", end - start)

    start = time.time()
    df.loc[df["A"] > 25, "calculation"] = df.loc[df["A"] > 25, ["A", "B", "C"]].sum(
        axis=1
    )
    df.loc[df["A"] <= 25, "calculation"] = df["A"] - df["B"] - df["C"]
    end = time.time()
    print("Time taken for vector change:", end - start)


if_else_vs_vector_comparison(1000)
print("Sub conclusion: Vectors are faster than for loops in Python")
_print_stars(50)


# comparison of matrix multiplication using for loops and vectors


def for_loop_matrix_comparison(n):
    A = np.random.randint(0, 50, size=(n, n))
    B = np.random.randint(0, 50, size=(n, n))

    start = time.time()

    C = np.zeros((n, n))

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i, j] = C[i, j] + A[i, k] * B[k, j]

    end = time.time()
    print("Time taken for for loop:", end - start)

    C = np.zeros((n, n))
    start = time.time()
    C = A @ B
    end = time.time()
    print("Time taken for vector change:", end - start)


print()
for_loop_matrix_comparison(4)
print("Sub conclusion: Vectors are faster than for loops in Python")
_print_stars(50)
