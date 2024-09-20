# Name: Prashant Gupta
# Program: PGupta_Program2.py
# Purpose: To calculate the closest flight departure and arrival time to the user input time and store the output in a text file
# Date: 18 April 2023


"""
funtion name: message
inputs: None
outputs: None
purpose: displays the welcome message with the list of available flights using the data from extract_times function
"""
def message():
    print("Welcome to closest flight finder.")
    print("The flights available are displayed in the table below.")
    print("Departure times", " " * 4, "Arrival times")
    dep_time, arrival_time = extract_times("flight_times.txt")
    for times in dep_time:
        alter_arrival_time = arrival_time[dep_time.index(times)]
        print(times, " " * 12, alter_arrival_time)


"""
function name: extract_times
inputs: name of the text file that stores the list of times
outputs: two different lists of the departure and arrival times
purpose: to extract the departure and arrival times from a text document and create two separate lists of departure and arrival times
"""
def extract_times(time_txt_file_as_str):
    # Two empty lists to store the departure and arrival times
    dep_times = []
    arrival_times = []

    # Open and read the text files
    with open(time_txt_file_as_str, "r") as flights:
        list_of_times = flights.readlines()

    # The end of departure time variable determines where the departure times end and arrival time starts in the text file
    end_of_dep_times = list_of_times.index("Arrival times,\n")

    for data in list_of_times:
        # Clean data variabe cleans the data from text file and stores just the data without the new lines or commas
        clean_data = data.split(",")[0]
        if clean_data != 'Departure times' and clean_data != "Arrival times":
            if list_of_times.index(data) < end_of_dep_times:
                dep_times.append(clean_data)
            else:
                arrival_times.append(clean_data)

    return dep_times, arrival_times


"""
function name: time_converter
inputs: any time as a string type
outputs: time passed since midnight from the input time
purpose: to convert any time provided as a string into minutes passed since midnight
"""
def time_converter(time_as_str):
    # Time variable here store the time part of the input excluding the time of day i.e. am/pm
    time = time_as_str.split()[0]
    hours = time.split(":")[0]
    mins = time.split(":")[1]

    time_since_midnight = int(hours) * 60 + int(mins)
    # This conditional statement determines if the time is in 12hr format and changes the time passed since midnight accordingly
    if len(time_as_str.split()) > 1:
        time_of_day = time_as_str.split()[1]
        if time_of_day == "pm" and hours != "12":
            time_since_midnight += 720

    return time_since_midnight


"""
function name: is_correct_format
inputs: user entered data
outputs: boolean value
purpose: checks if the user has typed in an invalid value and returns a boolean if the input is valid or not
"""
def is_correct_format(input_time):
    for char in input_time:
        try:
            if char != ":":
                int(char)
            
        except ValueError:
            return False
            break
    return True


def main():

    usr_time = input("Enter a 24hr time: ")
    if is_correct_format(usr_time):

        dep_time, arrival_time = extract_times("flight_times.txt")
        all_time_diff = []

        for time in dep_time:
            time_diff = abs(time_converter(usr_time) - time_converter(time))
            all_time_diff.append(time_diff)

        least_time_diff = min(all_time_diff)
        closest_dep_time = dep_time[all_time_diff.index(least_time_diff)]
        closest_arrival_time = arrival_time[all_time_diff.index(least_time_diff)]
        
        with open("closest_flight.txt", "w") as file:
            file.write("Closest departure time is " + closest_dep_time + ", arriving at " + closest_arrival_time + ".")
        
        check_another = input("Do you want to check another time?(y/n)")
        if check_another.lower() == "y":
            main()
    
    else:
        print("Invalid Format. Enter a 24hr Time (Ex. '13:15')")
        main()


message()
main()
