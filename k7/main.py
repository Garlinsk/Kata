#Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol.
# Hint: In Python you can use the string split method e.g my_email.split(“@”) or my_email(“@”)
# Once you learn functions, revisit this and write this code inside a function.

#BDD
  # Expected input from user-email.
  #  example 
  # age@gmail.com -Expected output-valid email
  #ambergmail.com-Expected output-invalid email


#pseudcode
 #define function that validates an email,
 #create a variable -my email to accept and store input,
 #create an if condition to check if the email is valid by using the split method,and store the value in a variable (email)
 #returns the variable 
 

def email():
    my_email = input("Enter email")

    if len(my_email.split("@")) > 1 and len(my_email.split(".")) > 1:
        return "valid email"
    else:
        return "invalid email"


results = email()
print(results)
