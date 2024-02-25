# time the python trick and cython trick

import time


def python_trick():
    for i in range(5000):
        for j in range(5000):
            result = i * j


# python trick

start_python = time.time()
python_trick()
end_python = time.time()


# cython trick  # cythonloop.pyx
# cimport cythonloop

import cythonloop


start_cython = time.time()
cythonloop.cython_trick()
end_cython = time.time()


print(f"Python time: {end_python - start_python: .6f}")
print(f"Cython time: {end_cython - start_cython: .6f}")
