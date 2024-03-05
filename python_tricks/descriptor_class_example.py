"""We can use the descriptor to ensure that the value of an attribute is always >= 0."""


class MyDescriptor:

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

        if value < 0:
            raise ValueError("Value must be >= 0")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:

    x = MyDescriptor()

    def __init__(self, num) -> None:
        self.x = num


if __name__ == "__main__":
    obj = MyClass(-1)
