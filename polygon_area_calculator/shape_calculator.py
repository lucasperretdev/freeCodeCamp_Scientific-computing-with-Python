class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2*self.width)+(2*self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        self.picture = ""
        if self.width <= 50 and self.height <= 50:
            for i in range(0, self.height):
                self.picture += "*"*self.width+'\n'
        else:
            self.picture = "Too big for picture."
        return self.picture

    def get_amount_inside(self, other_form):
        self.width_comparison = int(self.width / other_form.width)
        self.height_comparison = int(self.height / other_form.height)
        self.amount_inside = self.width_comparison*self.height_comparison
        return self.amount_inside

    def __str__(self):
        return f'Rectangle(width={str(self.width)}, height={str(self.height)})'


class Square(Rectangle):
    def __init__(self, lenght):
        self.width, self.height = lenght, lenght
        print("square init", self.width)

    def set_side(self, lenght):
        self.width, self.height = lenght, lenght

    def set_width(self, lenght):
        self.width, self.height = lenght, lenght

    def set_height(self, lenght):
        self.width, self.height = lenght, lenght

    def __str__(self):
        return f'Square(side={str(self.width)})'


# Tests
rect = Rectangle(3, 4)
other = Rectangle(10, 56)
print(rect)
print(rect.get_picture())
print(other)
print(other.get_picture())

sq = Square(10)
sq.set_side(5)
sq.set_height(6)
print(sq)
print(sq.get_picture())
