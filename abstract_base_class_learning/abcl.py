from abc import ABC, abstractmethod  # This is how you import for abstract base class


class Shape(ABC):
    @abstractmethod
    def area() -> int:
        pass


# sh = Shape()
# TypeError: Can't instantiate abstract class Shape without an implementation
# for abstract method 'area'


class Square(Shape):
    def __init__(self, length: int, bredth: int) -> None:
        super().__init__()
        self.length = length
        self.bredth = bredth

    def area(self):
        return self.length * self.bredth
