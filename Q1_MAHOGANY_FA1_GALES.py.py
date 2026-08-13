import math

#Asks for the X and Y values.
x1= float(input("Enter x1:"))
y1= float(input("Enter y1:"))
x2= float(input("Enter x2:"))
y2= float(input("Enter y2:"))

#This calculates for the Distance between X and Y.
distancex= float(x2 - x1)
distancey= float(y2 - y1)

distance= math.sqrt(math.pow(distancex, 2) + math.pow(distancey, 2))
print("The total distance is: ", distance)

#Reflection:
"""It was quite easy at the beginning but near the end it was quite frustrating since I couldnt understand what was wrong since I didnt notice anything wrong until a friend pointed out that I had an extra equals sign
 which was quite funny but atleast I learned what to watch out for. """