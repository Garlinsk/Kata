# Write a program that has an array or a list(only in python)  a = [5, 10, 15, 20, 25].
# Make a new array/list of only the first and last elements of the given array/list above.
# Once you learn functions, revisit this and write this code inside a function.


# BDD
# - get the list(user provided)
# - maninupulate to get the first and the last list items
# - return the new list


my_list = [5, 10, 20, 25]


def manipulate_list(my_list):
    # new_list = [my_list[0],my_list[-1]]
    new_list = [my_list.pop(0), my_list.pop()]
    return new_list


my_second_list = [50, 100, 20, 30]
result = manipulate_list(my_second_list)
print(result)
