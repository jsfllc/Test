"""
The purpose of this program is to find the real roots of
the values a, b, and c using the quadratic equation.
"""

import cmath

# Setting the user input equal to an integer and assigning that integer a variable.
a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))
d = b ** 2 - 4 * a * c  # discriminant


# Main method of the quadratic program, which calculates the real solutions of the program
# and returns the appropriate output.
def main():
    if d < 0:
        print("This equation has no real solution \n")
    elif d == 0:
        x = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print("This equation has one solutions: \n"), x
    else:
        x1 = (-b + cmath.sqrt((b ** 2) - (4.0 * (a * c)))) / (2.0 * a)
        x2 = (-b - cmath.sqrt((b ** 2) - (4.0 * (a * c)))) / (2.0 * a)
        print("This equation has two solutions: ", x1, " or ", x2, "\n")


if __name__ == '__main__':
    main()
