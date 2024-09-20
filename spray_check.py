# Name: Prashant Gupta
# Program: repetitive_spray_check.py
# Purpose: Check if pesticide can be sprayed from airplane and keep asking if the user wants to check another condition


again = True
while again:

    temp = int(input("Enter the temperature(in F): "))

    if temp < 70:
         print("Spraying is not possible.")
    else:
        humidity = int(input("Enter the humidity(in %): "))
        if humidity < 15 or humidity > 35:
              print("Spraying is not possible.")
        else:
            wind = int(input("Enter the wind speed(in mph): "))
            if wind > 10:
                 print("Spraying is not possible")
            else:
                 print("Spraying is possible.")

    should_continue = input("Do you want to start again?:(y/n) ").lower()
    if should_continue == "n":
        again = False

