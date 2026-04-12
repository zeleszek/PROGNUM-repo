import numpy as np

u = input()

l = np.array(['R', 'P', 'S']) #r beats s, p beats r, s beats p
i = np.random.randint(0, 3)
print(l[i])

if l[i] == u:
    print(f"draw, try again:)")
elif u == l[0]:
    if l[i] == l[1]:
        print(f"u loose:(")
    else:
        print(f"u win:)")
elif u == l[1]:
    if l[i] == l[2]:
        print(f"u loose:(")
    else:
        print(f"u win:)")
else:
   if l[i] == l[0]:
        print(f"u loose:(")
   else:
        print(f"u win:)") 