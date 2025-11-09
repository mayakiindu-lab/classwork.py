import math
a=float(input("Enter A: "))
b=float(input("Enter B: "))
height=float(input("Enter Height: "))
area=(1*(a+b)*height)/2
print(f'Area of Trapezium is: {round(area,3)}')
print('')
radius=float(input("Enter Radius: "))
areas=math.pi*radius**2
print(f'Area of the Circle is: {round(areas, 3)}')
print("")
print("Shaded Area = Trapezium's Area - Area of a Circle")
print('')
shadedarea=area-areas
print(f'Shaded area is: {round(shadedarea,3)}')