# Name: Prashant Gupta
# Program: registration.py
# Purpose: This program will complete the registration form and give out the temporary passwords

print("Registration Form")

# Take all the necessary information and store it
first_name = input("First Name: ")
last_name = input("Last Name: ")
date_of_birth = input("Birth Year: ")

# Use the information provided to display the message
print("Welcome", first_name, last_name + "!")
print("Your registration is complete.")
print("Your temporary password is:", first_name + "*" + date_of_birth)