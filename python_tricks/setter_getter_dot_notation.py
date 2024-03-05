class Circle:
    def __init__(self, radius):
        self.radius = radius


circle = Circle(10)
print(circle.radius)

circle.radius = -1
print(circle.radius)


# setter_getter_property.py
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value


circle = Circle(10)
print(circle.radius)

circle.radius = -1
