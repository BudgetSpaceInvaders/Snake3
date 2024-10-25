from math import *

t1 = float(input("Please insert the latitude of your first point: "))
t1 = pi / 180 * t1
g1 = float(input("Please insert the longitude of your first point "))
g1 = pi / 180 * g1
t2 = float(input("Please insert the latitude of your second point: "))
t2 = pi / 180 * t2
g2 = float(input("Please insert the longitude of your second point "))
g2 = pi / 180 * g2

distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print("The distance between the selected points is:", distance)