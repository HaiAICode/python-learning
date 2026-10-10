# Booleans will return True or False as results
#Example 1
print(8 > 3) # Output: True
print(8 < 3) # Output: False
print(8 == 3) # Output: False

#Example 2
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
print(f"Is {num} an even number? {is_even(num)}")