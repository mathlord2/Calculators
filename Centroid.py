import sympy

x, y = sympy.symbols("x y")

a = input("Enter Coordinates for point A (In form: x,y)")
b = input("Enter Coordinates for point B (In form: x,y)")
c = input("Enter Coordinates for point C (In form: x,y)")

a = list(map(int, a.split(",")))
b = list(map(int, b.split(",")))
c = list(map(int, c.split(",")))

midpointAB = [(a[0] + b[0])/2, (a[1] + b[1])/2]
midpointBC = [(b[0] + c[0])/2, (b[1] + c[1])/2]

#Slope = Rise/Run
slopeCnum_midAB = midpointAB[1]-c[1] #Rise from C to midpoint of AB
slopeCden_midAB = midpointAB[0]-c[0] #Run from C to midpoint of AB
slopeAnum_midBC = midpointBC[1]-a[1] #Rise from A to midpoint of BC
slopeAden_midBC = midpointBC[0]-a[0] #Run from A to midpoint of BC

eqCmidAB = sympy.Eq(slopeCnum_midAB * (x - midpointAB[0]) - slopeCden_midAB * (y - midpointAB[1]), 0)
#Calculates equation of line from C to midpoint of AB

eqAmidBC = sympy.Eq(slopeAnum_midBC * (x - midpointBC[0]) - slopeAden_midBC * (y - midpointBC[1]), 0)
#Calculates equation of line from A to midpoint of BC

print()

print("Point A lies on coordinates: " + str(a))
print("Point B lies on coordinates: " + str(b))
print("Point C lies on coordinates: " + str(c))

print()

print("The midpoint of points AB lie on: " + str(midpointAB))
print("The midpoint of points BC lie on: " + str(midpointBC))

print()

print("Equation 1: " + str(sympy.simplify(eqCmidAB)))
print("Equation 2: " + str(sympy.simplify(eqAmidBC)))

print()

print("The coordinates of the Triangle's Centroid are:\n " + str(sympy.linsolve([eqCmidAB, eqAmidBC], (x, y))))
