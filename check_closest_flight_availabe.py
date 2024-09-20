# Name: Prashant Gupta
# Class: CSCI 180 BQ
# Program: PGuptaProgram1.py
# Purpose : To take a time as input and show the closest flight departure time to the input time
# Date: 7 March 2023


# Print the list of available flight
print("Departure times", " " * 5, "Arrival times")
print("8:00 am", " " * 14, "10:16 am")
print("9:43 am", " " * 14, "11:52 am")
print("11:19 am", " " * 13, "1:31 pm")
print("12:47 pm", " " * 13, "3:00 pm")
print("2:00 pm", " " * 14, "4:08 pm")
print("3:45 pm", " " * 14, "5:55 pm")
print("7:00 pm", " " * 14, "9:20 pm")
print("9:45 pm", " " * 14, "11:58 pm")

# Take a time input from the user
input_time = input("Enter a 24-hour time: ")

# Convert the user input time to mins passed since midnight
hours = ""
mins = ""
position = 0
for char in input_time:
    if position == 0:
        if char != ":":
            hours += char
        else:
            position += 1
    else:
        mins += char

# Stores the user input time as mins passed since midnight
mins_passed_from_input_time = int(hours) * 60 + int(mins)

"""Take the absolute value of difference of mins passed since midnight of all the times from the user input time
Taking initial values as the first time from the available times as reference to start then updating it by checking every other value"""

diff1 = abs(mins_passed_from_input_time - 480)
minimum_diff = diff1
nearest_departure_time = "8:00 am"
nearest_arrival_time = "10:16 am"


diff2 = abs(mins_passed_from_input_time - 583)
if diff2 < minimum_diff:
    minimum_diff = diff2
    nearest_departure_time = "9:43 am"
    nearest_arrival_time = "11:52 am"


diff3 = abs(mins_passed_from_input_time - 679)
if diff3 < minimum_diff:
    minimum_diff = diff3
    nearest_departure_time = "11:19 am"
    nearest_arrival_time = "1:31 pm"


diff4 = abs(mins_passed_from_input_time - 767)
if diff4 < minimum_diff:
    minimum_diff = diff4
    nearest_departure_time = "12:47 pm"
    nearest_arrival_time = "3:00 pm"


diff5 = abs(mins_passed_from_input_time - 840)
if diff5 < minimum_diff:
    minimum_diff = diff5
    nearest_departure_time = "2:00 pm"
    nearest_arrival_time = "4:08 pm"


diff6 = abs(mins_passed_from_input_time - 945)
if diff6 < minimum_diff:
    minimum_diff = diff6
    nearest_departure_time = "3:45 pm"
    nearest_arrival_time = "5:55 pm"

diff7 = abs(mins_passed_from_input_time - 1140)
if diff7 < minimum_diff:
    minimum_diff = diff7
    nearest_departure_time = "7:00 pm"
    nearest_arrival_time = "9:20 pm"


diff8 = abs(mins_passed_from_input_time - 1305)
if diff8 < minimum_diff:
    minimum_diff = diff8
    nearest_departure_time = "9:45 pm"
    nearest_arrival_time = "11:58 pm"

# Print the closest flight time available
print("The closest departure time is", nearest_departure_time + ", arriving at", nearest_arrival_time + ".")
