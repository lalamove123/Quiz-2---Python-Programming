def calculate_area(length, width):
    return length * width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

area = calculate_area(l, w)
print("The area of the rectangle is:", area)
