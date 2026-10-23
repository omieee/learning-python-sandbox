from dataclasses import dataclass


class PlainService:
    def __init__(self, name, env):
        self.name = name
        self.env = env

    # Remember the __eq__ function is by default not generated


@dataclass
class Service:
    name: str
    env: str

    # We got __eq__, __repr__ and __init__ for free


a = PlainService("api", "prod")
b = PlainService("api", "prod")
print("plain:", a == b)

c = Service("api", "prod")
d = Service("api", "test")
print("dataclass:", c == d)
print(c)
