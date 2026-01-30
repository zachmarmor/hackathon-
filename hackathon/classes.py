class Grass:
    def __init__(self, state:int, eaten: bool, time_growth: str):
        self.state = state
        self.eaten = eaten
        self.time_growth = time_growth

class Animal:
    position: tuple
    age: int
    energy: int

class Sheep(Animal):
    def reproduction(self) -> None:
        if self.energy > main.seuil:
            self.energy += -20



class Wolf(Animal):
    pass