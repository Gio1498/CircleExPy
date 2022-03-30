class Circle:
    def __init__(self, radius = None, diameter = None):
        # Check if radius or diameter is given
        if radius is None and diameter is None:
            raise ValueError("Either radius or diameter must be specified")
        # Check if radius or diameter is a number
        elif radius is not None and diameter is not None:
            if type(radius) is str or type(radius) is str:
                raise TypeError("Parameter must be a number")
        # Create a new Circle object
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
            self.area = radius ** 2 * 3.14
        else:
            self.radius = diameter / 2
            self.diameter = diameter
            self.area = diameter ** 2 * 3.14

    # Print circle parameters
    def print_circle(self):
        print("---------------")
        print("Radius:", self.radius)
        print("Diameter:", self.diameter)
        print("Area:", self.area)
        print("---------------")
    