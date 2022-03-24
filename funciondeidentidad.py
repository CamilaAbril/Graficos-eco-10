import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-11, 11, 1)
a = 2
b = 9
c = 10
y = a*(x**2) + b*x + c 
 
print('Values of x: -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9  10', x)
print('Values of y: 153 120  91  66  45  28  15   6   1   0   3  10  21  36  55  78 105 136 171 210 253 300 ', y)
plt.plot(x, y)
plt.title("Quadratic Function")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()
