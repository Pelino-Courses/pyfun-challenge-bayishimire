import math


class Shape:
    import math
    """
    A base class for all shapes.
    """
    def _init_(self, name):
        """
        Initialize the shape with a name.
        """
        self.name = name
    def area(self):
        """
        Calculate the area of the shape.
        """
        raise NotImplementedError("Subclasses must be implemented this method.")
    def _str_(self):
        """
        Return a string representation of the shape.
        """
        return f"Shape: {self.name}"
class Circle(Shape):
    """
    A class to represnt a circle.
    """
    def _init_(self, radius):
        """
        initialize the circle with a radius.
        args:
            radius (float): The radius of the circle.
        """  
        super()._init_("Circle")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius
    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * (self.radius ** 2)
    def _str_(self):
        """
        Return a string representation of the circle.
        """
        return f"{super()._str_()}, Radius: {self.radius}, Area: {self.area():.2f}"
class Rectangle(Shape):
    """
    A class to represent a rectangle.
    """
    def _init_(self, width, height):
        """
        initialize the rectangle with width and height.
        args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super()._init_("Rectangle")
        if width <= 0 or height <=0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height
    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height
    def _str_(self):
        """
        Return a string representation of the rectangle.
        """
        return f"{super()._str_()}, Width: {self.width}, Height: {self.height}, Area: {self.area():.2f}"
class Triangle(Shape):
    """
    A class to represent a triangle.
    """
    def _init_(self, base, height):
        """
        Initialize the trianngle with base and height.
        args:
            base (float): The base of the triangle.
            height (float): The height of the triangle.
        """
        super()._init_("Triangle")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        self.base = base
        self.height = height
    def area(self):
        """
        Calculate the area of the triangle.
        """
        return 0.5 * self.base * self.height
    def _str_(self):
        """
        Return a string representation of the triangle.
        """
        return f"{super()._str_()}, Base: {self.base}, Height: {self.height}, Area: {self.area():.2f}"
    class Square(Shape):
        """
        A class to represent a square.
        """
        def _init_(self, side):
            """
            Initialize the square with a side length.
            args:
                side (float): The length of the side of the square.
            """
            super()._init_("Square")
            if side <= 0:
                raise ValueError("Side must be positive.")
            self.side = side
        def area(self):
            """
            Calculate the area of the square.
            """
            return self.side ** 2
        def _str_(self):
            """
            Return a string representation of the square.
            """
            return f"{super()._str_()}, Side: {self.side}, Area: {self.area():.2f}"