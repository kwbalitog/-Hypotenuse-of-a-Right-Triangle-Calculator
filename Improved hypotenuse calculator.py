import math

# Asks the user to enter a value for the first side of the triangle
side_a = int(input("Enter a length of side a: "))

# Asks the user to enter a value for the second side of the triangle
side_b = int(input("Enter a length of side b: "))

# Computes for the longest side of the triangle using the Pythagorean Theorem
c = math.sqrt(pow(side_a,2) + (pow(side_b,2)))

# Displays the results and rounds it to two decimal places
print(f"\n The hypotenuse is: {c: .2f}" )