# ignores the error of dividing 0 by 1
try:
    print(1/0)
# except statement for dividing by zero
except ZeroDivisionError:
    print("You cannot divide by zero")

try:
    x = int(input("Please enter a number: "))

# except statement for entering values
except ValueError:
    print("Please enter a valid integer!")
