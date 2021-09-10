#Create a function that takes in a list and print out the odd numbers in the given list

# we use  square brackets to create a list that contain intergers(odd numbers),and assign it to the variable(numbers)
# then the list is printed through the variable name.
# the strings are printed in the same order as they were stored in the list.


# odd_numbers=[0,1,3,5,7,9]

# print(odd_numbers)


#V# create a function that takes an argument(list)
# loop over the list (single number)
# divisible test of 2
# create a lnew list of odd number (empyty)
# if there is a remainder then its an odd number
# append the number to the newly created list
# return the new list


def list():
  list = int(input("Enter a number: "))

  if list % 2 == 0:
      results= "EVEN" 
      print(results)
  else:
      results= "ODD"  
      print(results)   
list()

