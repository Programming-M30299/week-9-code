from graphics import *


def displayMonths():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in months:
        print(month)


def displayTemperatureOfWeek():
    temperatures = [14.5, 8.0, -2.5, 15.0, 12.5, 9.0, -1.0]
    for temp in temperatures:
        print("It's {} degrees today".format(temp))
        if temp < 0:
            print("Brrrrr, that's freezing!")


def processNumbers():
    numbers = [11, 28, 32, 34, 45, 67, 70, 89, 90, 99]
    for i in range(len(numbers)):
        if i % 2 == 0:  # Only process numbers at even indexes
            square = numbers[i] ** 2
            print("The square of {} is {}".format(numbers[i], square))


def readPrime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        num = int(input("Enter a prime number less than 20: "))
        if num in primes:
            break
    print(num, "is a prime number less than 20")


def changeColours():
    win = GraphWin()
    circles = []
    for x in range(50, 200, 100):
        for y in range(50, 200, 100):
            circle = Circle(Point(x, y), 50)
            circle.setFill("red")
            circle.draw(win)
            circles.append(circle)  # Add the circle to the list

    for circle in circles:  # For each circle in the list
        win.getMouse()  # Wait for a mouse click
        circle.setFill("green")  # Change the colour of the circle
