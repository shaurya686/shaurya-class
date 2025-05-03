import math

# Ask the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter (circumference) of the circle: {perimeter:.2f}")
