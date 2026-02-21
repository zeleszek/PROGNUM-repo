Y1 = int(input("Y1 = "))
M1 = int(input("M1 = "))
D1 = float(input("D1 = "))

g = (M1 + 9)//12 + Y1
h = (M1 - 9)//7 + Y1
JD1 = (367 * Y1) - (7 * g // 4) - (3 * ((h//100) + 1)//4) + (275 * M1 // 9) + D1 + 1721029 - 0.5

Y2 = int(input("Y2 = "))
M2 = int(input("M2 = "))
D2 = float(input("D2 = "))

i = (M2 + 9)//12 + Y2
j = (M2 - 9)//7 + Y2
JD2 = (367 * Y2) - (7 * i // 4) - (3 * ((j//100) + 1)//4) + (275 * M2 // 9) + D2 + 1721029 - 0.5

NrD = JD2 - JD1

print(f"Julian Date 1 = {JD1}")
print(f"Julian Date 2 = {JD2}")
print(f"The number of days between the two given dates is: {NrD}")
