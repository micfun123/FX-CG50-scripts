xi = int(input("Enter the value of x1: "))  
yi = int(input("Enter the value of y1: "))
x2 = int(input("Enter the value of x2: "))
y2 = int(input("Enter the value of y2: "))

print("center are: ", (xi+x2)/2, (yi+y2)/2)
print("radius: ", ((x2-xi)**2 + (y2-yi)**2)**0.5)
print("area: ", 3.14*((x2-xi)**2 + (y2-yi)**2)**0.5)
print("gradient: ", (y2-yi)/(x2-xi))
print("equation: ", "(x-", (xi+x2)/2, ")^2 + (y-", (yi+y2)/2, ")^2 = ", ((x2-xi)**2 + (y2-yi)**2)**0.5)
print("bisector: ", "y = ", (y2-yi)/(x2-xi), "x + ", ((y2-yi)/(x2-xi))*((xi+x2)/2) - ((yi+y2)/2))

