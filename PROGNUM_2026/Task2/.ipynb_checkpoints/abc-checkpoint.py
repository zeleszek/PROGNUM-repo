from math import *

s1 = input("a =")
s2 = input("b =")
s3 = input("c =")

a = eval(s1)
b = eval(s2)
c = eval(s3)

D = b**2 - (4*a*c)
if D < 0 :
    print(f"there are no real solutions")
elif D > 0 :
    x1 = (-b - sqrt(D))/2*a
    x2 = (-b + sqrt(D))/2*a
    print(f" the solutions are x = {x1} and x = {x2}")
elif D == 0 :
    x = -b/2*a
    print(f" the solution is x = {x}")  