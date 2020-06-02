## python3 setup.py build_ext --inplace

def subtract(x, y):
    result = x - y
    return result

def list_subtract(x, y):
    result = []
    for i,el in enumerate(y):
        result.append(x[i] - el)
    return result

def np_subtract(x, y):
    result = x - y
    return result

def add (int x, int y):  # static typing
    cdef int result # static typing
    result = x + y
    return result