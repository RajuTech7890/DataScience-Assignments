# Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

inputstringMsg = print("Please Enter your Name....")
inputFirstName = input("First Name\n")
inputLastName = input("Last Name\n")
fullNameRev = inputFirstName[::-1]+" "+inputLastName[::-1]
print(fullNameRev)
