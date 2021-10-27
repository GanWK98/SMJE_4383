import math

radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumferences = 2* math.pi * radius_int
area = math.pi * (radius_int ** 2)

print ("The circumference is:",circumferences)
print ("The area is:",area)
