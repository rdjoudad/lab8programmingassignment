import math

"""
Geometry Calculator
Ryma Djoudad
Calculate the area and circumference of circles
3/8/2026
"""

def area(radius):
    circle_area = math.pi*(radius)**2
    return circle_area

def circumference(radius):
    circle_circumference = 2*math.pi*radius
    return circle_circumference