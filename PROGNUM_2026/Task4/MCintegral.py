import numpy as np
a = 0
b = 1

string = input("function with variable x:")
x = np.random.uniform(a, b, 10000)
f = eval(string)

i = (b - a)/len(x) * sum(f)

print(i)