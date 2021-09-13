# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
# Extras:
# If the number is a multiple of 4, display out a different message.
# Once you learn functions,revisit this and write this code inside a function.


#BDD
 #take 3 numbers from user,(user input)
 # place numbers in a list
 #sort the list -ranging(index 0-3)
 #pop out last no. of the list

#pseudcode 
 #define the function to find largest number,
 #declare variables to hold the list,
 #implement  a for-loop that add items in a list
 #Sort list 
 #Access the largest index in list

# (Method 1)
# def large_number():
#     l =[]
#     for y in range(0,3):
#         p=int(input('enter number \n'))
#         l.append(p)
#     numbers=sorted(l)
#     for x in numbers:
#         if x  % 4 ==0:
#             a=x
#             print(a,'Is a multiple of 4') 
   
#     print(numbers.pop())

# large_number() 

# (Method 2)
def large_number():
    first_number= int(input('Enter number \n'))
    second_number = int(input('Enter number \n'))
    third_number = int(input('Enter number \n'))
     
    list=[first_number,second_number,third_number]
    list.sort()
    print(list[-1])

large_number()    
 
  
 



