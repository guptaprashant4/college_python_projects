# Name: Prashant Gupta and Rojal Shrestha
# Program: five_click_house.py
# Purpose: To draw a house by clicking on the graphics window
# Date: 27 April 2023


from graphics import *


"""
Function: frame
Input: Graphic window
Output: Two end points of the rectangle
Purpose: To get two points inputs from mouse click and draw a rectangle
"""
def frame(win):
    point1 = win.getMouse()
    point2 = win.getMouse()
    house_frame = Rectangle(point1, point2)
    house_frame.draw(win)
    return point1, point2


"""
Function: door
Input: Graphic Window
Output: Points obtained from frame function, length of the door and two end points of the door
Purpose: To get a point as input from mouse click and draw a rectangle one-third of the frame 
"""
def door(win1):
    p1, p2 = frame(win1)
    length = (p2.getX() - p1.getX()) / 3

    door_not_drawn = True
    while door_not_drawn:
        door_centre = win1.getMouse()
        door_p1x = door_centre.getX() - (length/2)
        door_p1y = door_centre.getY()
        door_p2x = door_centre.getX() + (length/2)
        door_p2y = p2.getY()

        if door_p1x < p1.getX() or p2.getX() < door_p2x or door_centre.getY() < p1.getY() or door_centre.getY() > p2.getY():
            message_window = GraphWin(width=600, height=400, title="Error!")
            message = Text(Point(300,200), "The door can not be outside the house frame!")
            message.draw(message_window)
        else: 
            door = Rectangle(Point(door_p1x, door_p1y), Point(door_p2x, door_p2y))
            door.draw(win1)
            door_not_drawn = False
    return p1, p2, length, door.p1, door.p2


"""
Function: window
Input: Graphic Window
Output: End points of the frame
Purpose: To create a square window from a mouse click as the centre of the window
"""
def window(win2):
    frame_p1, frame_p2, len_of_door, door_p1, door_p2 = door(win2)
    len_of_window = len_of_door / 2

    window_not_drawn = True
    while window_not_drawn:
        center_of_window = win2.getMouse()
        p1x = center_of_window.getX() - len_of_window/2
        p2x = center_of_window.getX() + len_of_window/2
        p1y = center_of_window.getY() - len_of_window/2
        p2y = center_of_window.getY() + len_of_window/2

        if frame_p1.getX() > p1x or p2x > frame_p2.getX() or frame_p1.getY() > p1y:
            message_window = GraphWin(width=600, height=400, title="Error!")
            message = Text(Point(300,200), "Window can only be inside the house!")
            message.draw(message_window)
        
        elif p2y > door_p1.getY():
            message_window = GraphWin(width=600, height=400, title="Error!")
            message = Text(Point(300,200), "Window can not be below the door!")
            message.draw(message_window)

        else:
            window_frame = Rectangle(Point(p1x, p1y), Point(p2x, p2y))
            window_frame.draw(win2)
            window_not_drawn = False
    return frame_p1, frame_p2


"""
Funtion: roof
Input: Graphic Window
Output: None
Purpose: Draw a roof using the two end points of the frame
"""
def roof(win3):
    p1, p2 = window(win3)

    roof_not_drawn = True
    while roof_not_drawn:
        point = win3.getMouse()
        dy = p1.getY()
        dx = p2.getX()
        if point.getY() > p1.getY():
            message_window = GraphWin(width=600, height=400, title="Error!")
            message = Text(Point(300,200), "The roof has to be above the house!")
            message.draw(message_window)
        else:
            triangle = Polygon(p1, Point(dx, dy), point)
            triangle.draw(win3)
            roof_not_drawn = False


"""
Function: graphics_window
Input: None
Output: None
Purpose: Create a graphic window and initalize the roof function inside it
"""
def graphics_window():
    win = GraphWin(width=800, height=800, title="Five Click House")
    roof(win)
    win.getMouse()


def main():
    graphics_window()


main()
