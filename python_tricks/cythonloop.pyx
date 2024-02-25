
def cython_trick():
    cdef int i, j
    for i in range(5000):
        for j in range(5000):
            result = i * j


if __name__ == '__main__':
    cython_trick()
    print('done')

