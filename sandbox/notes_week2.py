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

### translation with broadcasting ###

rawdat = np.genfromtxt('../numpy/broadcast-translation/points_circle.dat')
#x,y = rawdat[:,0],rawdat[:,1]

dat = np.zeros_like(rawdat)

transVec = np.array([2.1,1.1])

dat = rawdat+transVec

fig,ax = plt.subplots()

ax.plot(*rawdat.T,marker='o',ls='')
ax.plot(*dat.T,marker='x',ls='')
plt.show(block=False)

### I/O ###

rawdat = np.loadtxt('../numpy/input-output/xy-coordinates.dat')
rawdat[:,1] +=2.5
np.savetxt('./xy-coordinates_shifted.dat', rawdat, fmt='%.6f', header='modified data')

### Random number generators ###

a = np.random.random((2,2))
print(a)

b = np.random.choice(np.arange(4), 10) # choose provded N x randomly from a provided list
print(b)

### ###

a = np.random.random((10000))
b = np.random.randn((10000))

def xtract(A, binW=10):
    fig,ax=plt.subplots()
    m = np.mean(A)
    s = np.std(A)
    ax.hist(A,bins=int(A.size/binW))
    dy = np.diff(ax.get_ylim())
    ax.axvline(x=m, ls=':', color='red')
    ax.axvline(x=m-s, ls=':', color='red')
    ax.axvline(x=m+s, ls=':', color='red')
    ax.text(m,dy/2,'mean: {0:.2f}'.format(m))
    ax.text(m,dy/3,'std.dev.: {0:.2f}'.format(s))
    
    return fig

xtract(a, binW=100)
xtract(b, binW=100)

### linear-algebra ###

A = np.random.random((2,2))
B = np.random.random((2,2))

Asym = A+A.T
Bsym = B+B.T

C = np.dot(Asym,Bsym)

eigs = np.linalg.eigvals(C)
print("Eigenvalues are: " + str(eigs))

### Temporary arrays ###

a = np.random.random((1024, 1024, 50))
b = np.random.random((1024, 1024, 50))
c = (np.sin(a) + np.cos(b)) + 2.0 * a - 4.5 * b


### Numexpr

x = np.random.random((1000000, 1))
y = np.random.random((1000000, 1))

import numexpr
poly = numexpr.evaluate("((.25*x + .75)*x - 1.5)*x - 2")


