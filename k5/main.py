# TASK 9:
# Write a program that takes the age in years and returns the age in days.Use 365 days as the length of a year for this challenge as we would like to ignore leap years. Only accept positive numbers.


# BDD
# Get an input of the users age
# Verify that the age is positive
# Output their age in days

# Pseudocode
# Input for user
# Either use a built in method to test if positive or use an if statement
# Multiply the age by 365
# Show an output of the age

def years():
  years = int(input('How old are you? \n'))

  if years > 0:
    years_in_days = years * 365
    print(f'You are { years_in_days } days old.')
  else:
    print('Please input a valid age above 0')


years()
