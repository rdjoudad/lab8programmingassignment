"""
Geometry Calculator
Ryma Djoudad
Calculate the area and circumference of circles and rectangles using a user-friendly interface
3/8/2026
"""

import circle as cir, rectangle as rec
# Using aliases in this case is necessary as both circle and rectangle have the function area
# It can get confusing telling which is which, so using shortened versions of the file names when importing is ideal
while True:
    print("Geometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")

    user_choice = int(input("Enter your choice (1-5): "))

    if user_choice == 1:
        r = float(input("Enter the radius of the circle: "))
        print(f"Your circle's area is: {cir.area(r):.2f}")
        input("Press Enter to continue... ")
    elif user_choice == 2:
        r = float(input("Enter the radius of the circle: "))
        print(f"Your circle's circumference is: {cir.circumference(r):.2f}")
        input("Press Enter to continue... ")
    elif user_choice == 3:
        l = float(input("Enter the length of the rectangle: "))
        w = float(input("Enter the width of the rectangle: "))
        print(f"Your rectangle's area is: {rec.area(l, w):.2f}")
        input("Press Enter to continue... ")
    elif user_choice == 4:
        l = float(input("Enter the length of the rectangle: "))
        w = float(input("Enter the width of the rectangle: "))
        print(f"Your rectangle's perimeter is: {rec.perimeter(l, w):.2f}")
        input("Press Enter to continue... ")
    elif user_choice == 5:
        print("Goodbye!")
        break
