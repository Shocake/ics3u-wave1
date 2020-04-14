import math
radius = float(input("What is the cylinders radius?"))
height = float(input("What is the cylinders height?"))

volume = str(round(math.pi * radius * radius * height, 1))
print("The cylinder's volume is approximately " + volume + " units cubed.")