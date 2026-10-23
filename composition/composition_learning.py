class Engine:
    def __init__(self, horse_poser: int) -> None:
        self.horse_power = horse_poser


class Car:
    def __init__(self, make: str, model: str, horse_power: int) -> None:
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)

    def display(self) -> str:
        return f"I own a {self.make} {self.model}, \
            which is {self.engine.horse_power} CC"
