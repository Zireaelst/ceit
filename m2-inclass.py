

print('A SIMPLE PROGRAM')

print('This program is developed to compute the area of a triangle and a rectangle. The properties of these shapes will be provided by the user.')

print('--Computing Triangle Area--')
print('Enter height and base for the triangle. The area will be printed immediately.')

a = float(input("Enter height"))
b = float(input("Enter base"))
areaoftri = (a * b) / 2

print("The are of triangle is:", areaoftri)

print("--Computing Rectangle Area--")
print("Enter width and length for the rectangle. The area will be printed immediately")

c = float(input("Enter width"))
d = float(input("Enter length"))
areaofrec = (c * d)
print("The area of the rectangle is:", areaofrec)

print("**********************")
print("The program ends.")
