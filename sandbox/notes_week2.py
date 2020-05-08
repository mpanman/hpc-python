import timeit
import numpy as np
from matplotlib import pyplot as plt
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

### Differentiation ###
xi = np.arange(0,np.pi/2+0.1,0.1)
dx = np.abs(xi[0]-xi[-1])/(xi.size-1)
def deriv_1(x, dx, func):
    return (func(x+dx)-func(x-dx))/(2*dx)

def deriv(numFunc,dx):
    return (numFunc[2:]-numFunc[:-2])/(2*dx)

#s = deriv_1(xi,np.sin)
#c = deriv_1(xi,np.cos)

s = deriv(np.sin(xi),dx)
c = deriv(np.cos(xi),dx)

plt.figure()
plt.plot(xi[1:-1], s, label='int(sin)', color='C0')
plt.plot(xi, np.sin(xi), label='sin', color='C0',ls=':')
plt.plot(xi[1:-1], c, label='int(cos)', color='C1')
plt.plot(xi, np.cos(xi), label='cos', color='C1',ls=':')
plt.legend()
plt.show(block=False)

### Integration ###
a  = 0
b  = np.pi/2
dx = 0.01

xi  = np.arange(a,b,dx)
xip = (xi[1:]+xi[:-1])/2.

s = np.sum(np.sin(xip))*dx
print("Riemann sum: {0:f}".format(s))

### array manipulation ###

a   = np.arange(8*8).reshape(8,8)
b,c = np.split(a, 2, axis=0)
ar  = np.concatenate((b,c), axis=0)

b1,c1 = np.split(a, 2, axis=1)
ar1  = np.concatenate((b1,c1), axis=1)
