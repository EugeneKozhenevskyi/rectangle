class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def area(self) -> int:
        return self.a * self.b

    def perimeter(self) -> int:
        return 2 * self.a + 2 * self.b
