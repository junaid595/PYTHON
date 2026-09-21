# Function to check right-angled triangle

def check_right_triangle(a, b, c):
    # Find the largest side
    sides = [a, b, c]
    sides.sort()

    # Check Pythagorean theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False


# Taking input
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Function calling
if check_right_triangle(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
