numbers = []

for i in range(5):
    num = int(input("Input a number: "))
    numbers.append(num)

numbers.sort(reverse=True)

print("Sorted numbers (highest to lowest):", numbers)
