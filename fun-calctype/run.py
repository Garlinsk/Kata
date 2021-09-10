# You have to create a function calcType, which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them(also a number).

# Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

# The possible return strings are: "addition", "subtraction", "multiplication", "division".


##BDD
##create a function
# eg-def calcType(a,b,c):
## use if statements
##to check for addition; if(a+b)== c result be addition
##Return the results
## 


#pseudocode
  #define function
  #assign variables value to be input
  #print strings results

def calcType():
    a = int(input("Enter number\n"))
    b = int(input("Enter  another number\n"))
    c = int(input("Enter  a third number\n"))

    if a + b == c:
        results = "addition"
    elif a - b == c:
        results = "substraction"
    elif a * b == c:
        results = "multiplication"
    elif a / b == c:
        results = "division"
    else:
        results = "Check your inputs "
    print(results)


calcType()
