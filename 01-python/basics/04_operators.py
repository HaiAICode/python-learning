# Arithmetic Operators
x , y = 10, 3
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)

# Assignment Operators
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"There are {count} numbers in the list.")

# Ternary Operators
num = 5
day = int(input("Enter a number (1-7) to represent a day of the week: "))
day = "Weekday!" if day >= 5 else "Weekend!"
print(day)
