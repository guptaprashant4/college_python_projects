# college_python_projects

A collection of Python programs written for an introductory Python programming course (CSCI 180) at college.

---

## Projects

### Temperature Converter — `F_to_C_Converter.py`
Converts a Celsius temperature entered by the user to Fahrenheit.

```
$ python F_to_C_Converter.py
This program will convert a Celsius temperature entered by the user to Fahrenheit.
What is the Celsius temperature? 100
The temperature is 212.0 degrees Fahrenheit.
```

---

### Closest Flight Finder — `check_closest_flight_availabe.py`
Displays a schedule of available flights and finds the closest departure time to a user-provided 24-hour time.

```
$ python check_closest_flight_availabe.py
Departure times        Arrival times
8:00 am                10:16 am
...
Enter a 24-hour time: 14:00
The closest departure time is 2:00 pm, arriving at 4:08 pm.
```

A refactored version of this program is also available in the `check_closest_flight_modified/` folder.

---

### Distance Calculator — `distance.py`
Calculates the straight-line (Euclidean) distance between two points on a 2D plane.

```
$ python distance.py
Enter the first set of points
Example: 2,4
=> 0,0
Enter the second set of points
=> 3,4
The distance between the points is 5.0 units.
```

---

### Registration Form — `registration.py`
Simulates a basic registration form. Takes a user's first name, last name, and birth year, then generates a temporary password.

```
$ python registration.py
Registration Form
First Name: Prashant
Last Name: Gupta
Birth Year: 2004
Welcome Prashant Gupta!
Your registration is complete.
Your temporary password is: Prashant*2004
```

---

### Draw a House — `draw_a_house/`
Uses Python's Turtle graphics module to draw a house.

---

### Other Scripts

| File | Description |
|---|---|
| `functions.py` | Practice with defining and calling functions |
| `numbers.py` | Basic number operations and exercises |
| `spray_check.py` | Miscellaneous exercise from coursework |
| `closest_flight.txt` | Data file used by the flight finder program |

---

## Requirements

- Python 3.x
- No external libraries required (standard library only)

---

## Running a Script

```bash
python <script_name>.py
```

For example:

```bash
python distance.py
```

---

## Course

**CSCI 180** — Introductory Python Programming
