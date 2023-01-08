class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape):
        return int(self.get_area()/shape.get_area())

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def get_area(self):
        return super().get_area()

    def get_diagonal(self):
        return super().get_diagonal()

    def get_perimeter(self):
        return super().get_perimeter()

    def get_picture(self):
        return super().get_picture()

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

