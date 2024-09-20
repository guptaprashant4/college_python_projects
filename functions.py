# Name: Prashant Gupta
# Program: functions.py
# Purpose: To perform different taks from the fucntions listed
# Date: 30 March 2023


def nurseryRhyme():
    print("Mary had a little lamb,")
    print("Its fleece was white as snow, yeah.")
    print("Everywhere the child went,")
    print("The little lamb was sure to go, yeah.")
    print()
    print("He followed her to school one day,")
    print("And broke the teacher's rule.")
    print("What a time did they have,")
    print("That day at school.")
    print()
    print("Tisket, tasket,")
    print("A green and yellow basket.")
    print("Sent a letter to my baby,")
    print("On my way I passed it.")

def drawTree():
    for num in range(1, 9):
        if num == 7 or num == 8:
            print("**")
        else:
            print(num * "*")


def pdsToOzs(lb_weight):
    oz_weight = lb_weight * 16
    return round(oz_weight, 2)


# This functions will display a list of fuctions that can be carried out
def main():
    print('1 Write the words of the rhyme "Mary had a little lamb"')
    print("2 Draw a christmas tree")
    print("3 Convert pounds to ounces")
    print("4 Exit")

    keep_running = True
    while keep_running:
        selection = input("Choose what you'd like to do from the menu: ")
        if selection == '1':
            nurseryRhyme()
        elif selection == '2':
            drawTree()
        elif selection == '3':
            pounds = eval(input("Enter the weight in lbs: "))
            ounce = pdsToOzs(pounds)
            print(f'{pounds}lbs will be equal to {ounce}ozs.')
        elif selection == '4':
            keep_running = False
        else:
            print("Select any number from the menu above.")
            
main()