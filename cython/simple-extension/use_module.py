from cyt_module import subtract
from cyt_module import list_subtract
import numpy as np
z = subtract(5, 2)
print(z)

a = [5, 6, 7, 8]
b = [1, 2, 3, 4]

z1 = list_subtract(a, b)
print(z1)

c = np.arange(100)
d = np.arange(100, 200)

z2 = list_subtract(c, d)
print(z2)