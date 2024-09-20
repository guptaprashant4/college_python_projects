# Name: Prashant Gupta
# Program: numbers.py
# Purpose: To determine whether an user input number is contained in a list and add it to the list if desired
# Date: 30 March 2023

list_of_num = [10, 21, 28, 9, 6, 11, 18, 30, 28, 2]

# Takes an integer input from the user
user_num = int(input("Ente a number between 0-30: "))

again = True
while again:

    # Checks if the user input number is contained in the list
    if user_num in list_of_num:
        print("This number is in the list.")

    else:
        print("This number is not in the list")

        # Asks the user if to add the input number to the list
        add_to_list = input("Do you want to add this number to the list?(y/n) ")
        if add_to_list.lower() == "y":
            list_of_num.append(user_num)
            list_of_num.sort()
            print(list_of_num)
    
    # Asks the user whether to continue checking more numbers or quit the program
    add_more = input("Do you want to check more nums?(y/n) ")
    if add_more.lower() == "y":
        user_num = int(input("Ente a number between 0-30: "))
    else:
        again = False