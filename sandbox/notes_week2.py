import timeit
import numpy as np

#timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

arr = np.arange(1000)
difl = np.zeros(999, int)
#difa = np.zeros(999, int)

def diff_loop(arr, difl):
    for i in __builtin__.range(1, len(arr)):
        difl[i-1] = arr[i] - arr[i-1]
    return difl

def diff_array(arr):
    return arr[1:] - arr[:-1]

#l = timeit.timeit("'diffl = diff_loop(arr, difl)'", number=1000)
#a = timeit.timeit("'diffa = diff_array(arr)'", number=1000)
#
f1 = """for i in range(1, len(arr)): difl[i-1] = arr[i]-arr[i-1] """
f2 = """arr[1:] - arr[:-1] """

prequel = """
import numpy as np
arr = np.arange(1000)
difl = np.zeros(999, int)
"""

l = timeit.timeit(f1, number=1000, setup=prequel)
a = timeit.timeit(f2, number=1000, setup=prequel)

## %timeit gives you the statistics
# %timeit diff_loop(arr, difl)
# %timeit diff_array(arr)