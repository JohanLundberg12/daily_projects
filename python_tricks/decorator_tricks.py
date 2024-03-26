import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    import time
    import functools
    from functools import wraps
    from joblib import Memory
    return Memory, functools, np, time, wraps


@app.cell
def __(time, wraps):
    def timer(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            print(f"Execution time of {function.__name__}: {end - start} seconds")
            return result
        return wrapper

    def debug(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper
    return debug, timer


@app.cell
def __(Memory, np, timer):
    size = 2000
    a = np.random.rand(size, size)
    b = np.random.rand(size, size)

    cachedir = '/tmp/joblib_cache'
    memory = Memory(cachedir, verbose=0)

    @timer
    #@debug
    @memory.cache
    def matrix_mult(a, b):
        return np.dot(a,b)

    result = matrix_mult(a, b)
    return a, b, cachedir, matrix_mult, memory, result, size


@app.cell
def __(functools, timer):
    # fibonacci is an expensive operation which is why caching is useful here.
    # A standard for loop on the other hand, doing multiplications of i*j, 
    # is a less expensive computation, so a cache lookup does not benefit us here as it is likely more expensive than doing the computation again. 

    @timer
    @functools.lru_cache(maxsize=128)  # Limit cache size
    def fibonacci(n):
        """Calculates the nth Fibonacci number (expensive for large n)"""
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


    fibonacci(10)
    return fibonacci,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
