# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade:
# A > 79, B - 60 to 79, C - 59 to 49, D - 40 to 49, E - less 40

#BDD
 #
         
# if avg >= 79 and avg <= 100:
#     print("Your Grade is A")
# elif avg >= 60 and avg < 79:
#     print("Your Grade is B")
# elif avg >= 49 and avg < 59:
#     print("Your Grade is C")
# elif avg >= 40 and avg < 49:
#     print("Your Grade is D")
# elif avg >= 0 and avg < 40:
#     print("Your Grade is E")

# else:
#     print("Invalid Input!")


# BDD
# input = >79  output = A
# PSEUDOCODE
# - define a function that validate user to calculate the marks.
# - create a variable - marks1 to accept and store the marks from the user, marks2, marks3, marks4, marks5 and then get the total, then do an average of the five marks.
# - create an if condition to check if the average marks entered are correct and return the grades
# - return the grade
# 10: 26


def marks():

    marks1 = int(input(‘Enter marks1 \n’))
    marks2 = int(input(‘Enter marks2 \n’))
    marks3 = int(input(‘Enter marks3 \n’))
    marks4 = int(input(‘Enter marks4 \n’))
    marks5 = int(input(‘Enter marks5 \n’))

    if marks1 >= 0 and marks1 <= 100 and marks2 >= 0 and marks2 <= 100 and marks3 >= 0 and marks3 <= 100 and marks4 >= 0 and marks4 <= 100 and marks5 >= 0 and marks5 <= 100:
        avg = (marks1 + marks2 + marks3 + marks4 + marks5)/5
    else:
        print(‘Invalid entry!’)
    if avg > 79:
        print(‘Your grade is A’)
    elif avg >= 60 and avg <= 79:
        print(‘Your grade is B’)
    elif avg > 49 and avg <= 59:
        print(‘Your grade is C’)
    elif avg >= 40 and avg <= 49:
        print(‘Your grade is D’)
    else:
        print(‘Your grade is E’)
        
marks()
