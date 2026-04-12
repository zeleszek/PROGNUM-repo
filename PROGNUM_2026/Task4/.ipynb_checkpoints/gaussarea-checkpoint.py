import numpy as np
from matplotlib.pyplot import figure, show, savefig
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
   return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

A = 1.0
x0 = 0.0
sig = 2.0
z0 = 0.0
x = np.linspace(-10, 10, 200)
f = gauss(x, A, x0, sig, z0)
a = np.linspace(0, 2.5)
g = gauss(a, A, x0, sig, z0)

fig = figure()
frame = fig.add_subplot(1,1,1)
frame.plot(x, f)
frame.fill_between(a, g, 0, facecolor='pink')
savefig("gauss_plot.png", dpi=300, bbox_inches="tight")
show()

area, error = quad(gauss, 0, 2.5, args=(A, x0, sig, z0,))
print(f"area between 0 and 2.5:", area)
print()

b, err = quad(gauss, -np.inf, np.inf, args=(A, x0, sig, z0,))
print(f"area between negative and positive infinity using quad():", b)

#6:
a_6 = A*sig * np.sqrt(2*np.pi)
print(f"area between infinities using the formula:", a_6)
print(f"area found using quad = area calculated:", b == a_6, f", but the difference is very small")