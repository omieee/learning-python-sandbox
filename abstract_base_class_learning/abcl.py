from abc import ABC, abstractmethod  # This is how you import for abstract base class


class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass


# sh = Shape()
# TypeError: Can't instantiate abstract class Shape without an implementation
# for abstract method 'area'


class Square(Shape):
    def __init__(self, side: int) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side * 2
