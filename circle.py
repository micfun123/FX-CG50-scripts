xi = float(input("Enter the value of x1: "))  
yi = float(input("Enter the value of y1: "))
x2 = float(input("Enter the value of x2: "))
y2 = float(input("Enter the value of y2: "))

center = ((xi + x2) / 2, (yi + y2) / 2)
radiusfromcenter = ((x2 - xi) ** 2 + (y2 - yi) ** 2) ** 0.5
area = 3.14159 * radiusfromcenter ** 2
gradient = (y2 - yi) / (x2 - xi)
equation = "y = " + str(gradient) + "x + " + str(yi - gradient * xi)
bisector = "y = " + str(-1 / gradient) + "x + " + str(yi - (-1 / gradient) * xi)
#print to 2 decimal places
print("Center: ({:.2f}, {:.2f})".format(center[0], center[1]))
print("Radius: {:.2f}".format(radiusfromcenter))
print("Area: {:.2f}".format(area))
print("Equation: " + equation)
print("Bisector: " + bisector)
