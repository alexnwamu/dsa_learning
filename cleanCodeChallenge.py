class Coordinates:
    def __init__(self, xAxis, yAxis):
        self.xAxis = xAxis
        self.yAxis = yAxis


class Rectangle:
    def __init__(self, starting_point, breadth, height):
        self.starting_point = starting_point
        self.breadth = breadth
        self.height = height

    def getArea(self):
        return self.breadth * self.height

    def print_coordinates(self):
        top_right = self.starting_point.xAxis + self.breadth
        bottom_left = self.starting_point.yAxis + self.height
        print('Starting Point (X)): ' + str(self.starting_point.xAxis))
        print('Starting Point (Y)): ' + str(self.starting_point.yAxis))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def create_rectangle():
    main_point = Coordinates(50, 100)
    newRectangle = Rectangle(main_point, 90, 10)

    return newRectangle


rectangle = create_rectangle()

print(rectangle.getArea())
rectangle.print_coordinates()