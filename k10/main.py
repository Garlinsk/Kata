# TASK 10: 
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.


### BDD
# Get user input (base and height)
# Calculate based on the inputs
#  Return the are as the result

### Pseudo code
# Create a function:
# - prompt for height & base then store in variables
# - convert to float for manipulation
# - Calculate
# - Return response

def calculateArea():
    base = float(input("Enter your base value: "))
    height = float(input("Enter the height value: "))

    area = 0.5 * base * height

    return area


result = calculateArea()

print(result)
