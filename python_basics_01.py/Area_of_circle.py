"""
import math
class Area_of_circle:
    def __init__(self,r):
        self.r = r
    def Area(self):
        X = float((22/7)*(self.r**2))
        print(f"Area of circle with radius {self.r} is {X}")

A = Area_of_circle(int(4))
print(A)
#t = float(input("Please enter the radius of the circle"))
 """
from math import pi
R = float(input("Please enter the radius of the circle"))
A = float(pi*(R**2))
print(f"Area of the circle with radius {R} is {A}")
