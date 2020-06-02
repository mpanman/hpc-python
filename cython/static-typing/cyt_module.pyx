def subtract(x, y):
    result = x - y
    return result

def subtract_i(int x, int y):
    cdef int result

    result = x - y
    
    return result

def subtract_f(float x, float y):
    cdef float result
    result = x - y

    return result

