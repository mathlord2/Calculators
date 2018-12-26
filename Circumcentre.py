#Created by @mathlord2
import sympy

x, y = sympy.symbols("x y")

a = input("Enter the coordinates for point A (in form x,y):")
b = input("Enter the coordinates for point B (in form x,y):")
c = input("Enter the coordinates for point C (in form x,y):")

d = list(map(int, a.split(",")))
e = list(map(int, b.split(",")))
f = list(map(int, c.split(",")))

g = [(d[0]+e[0])/2, (d[1]+e[1])/2] #Midpoint of AB
h = [(e[0]+f[0])/2, (e[1]+f[1])/2] #Midpoint of BC

#Slope = Rise/Run
ySlopeAB = e[1]-d[1] #Rise of AB
xSlopeAB = e[0]-d[0] #Run of AB
ySlopeBC = f[1]-e[1] #Rise of BC
xSlopeBC = f[0]-e[0] #Run of BC             

eqPBofAB = sympy.Eq(xSlopeAB * (x - g[0]) + ySlopeAB * (y - g[1]), 0)
#Calculates equation of perpendicular bisector of AB

eqPBofBC = sympy.Eq(xSlopeBC * (x - h[0]) + ySlopeBC * (y - h[1]), 0)
#Calculates equation of perpendicular bisector of BC

print ("The coordinates for Point A are: " + str(d))
print ("The coordinates for Point B are: " + str(e))
print ("The coordinates for Point C are: " + str(f))

print("The midpoint of points AB lie on: " + str(g))
print("The midpoint of points BC lie on: " + str(h))

print("Equation 1: " + str(sympy.simplify(eqPBofAB)))
print("Equation 2: " + str(sympy.simplify(eqPBofBC)))

print ("The coordinates for the triangle's circumcentre is: " + str(sympy.linsolve([eqPBofAB, eqPBofBC], (x, y))))
