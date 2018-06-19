
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3
import numpy as np
constDiameter = 12
radius = constDiameter/2
volumeSphere = (4/3 * np.pi * radius ** 3)
print("The Volume of spher is .." + str(volumeSphere) + "cubic cm")
