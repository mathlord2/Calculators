import sympy

x, y = sympy.symbols("x y")

a = input("Enter Coordinates for point A (In form: x,y)")
b = input("Enter Coordinates for point B (In form: x,y)")
c = input("Enter Coordinates for point C (In form: x,y)")

a = list(map(int, a.split(",")))
b = list(map(int, b.split(",")))
c = list(map(int, c.split(",")))

#Slope = Rise/Run
ySlopeAB = b[1]-a[1] #Rise of AB
xSlopeAB = b[0]-a[0] #Run of AB
ySlopeBC = c[1]-b[1] #Rise of BC
xSlopeBC = c[0]-b[0] #Run of BC

eqCmidAB = sympy.Eq(xSlopeAB * (x - c[0]) + ySlopeAB * (y - c[1]), 0)
#Calculates equation of altitude from C to AB

eqAmidBC = sympy.Eq(xSlopeBC * (x - a[0]) + ySlopeBC * (y - a[1]), 0)
#Calculates equation of altitude from A to BC

print("Point A lies on coordinates: " + str(a))
print("Point B lies on coordinates: " + str(b))
print("Point C lies on coordinates: " + str(c))

print("Equation 1: " + str(sympy.simplify(eqCmidAB)))
print("Equation 2: " + str(sympy.simplify(eqAmidBC)))

print("The coordinates of the Triangle's Orthocentre are:\n " + str(sympy.linsolve([eqCmidAB, eqAmidBC], (x, y))))
