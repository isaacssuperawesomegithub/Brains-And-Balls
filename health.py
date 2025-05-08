class Health:
    def __init__(self, starting_hp: int):
        self.hp = starting_hp
        Health.instance = self


    def __add__(self, other):
        return self.hp + other

    def __iadd__(self, other):
        self.hp += other


    def __sub__(self, other):
        return self.hp - other

    def __isub__(self, other: float):
        self.hp -= other


    def __set__(self, other):
        self.hp = other


    def __lt__(self, other: float):
        return self.hp < other
    
    def __gt__(self, other: float):
        return self.hp > other

    def __le__(self, other: float):
        return self.hp <= other
    
    def __ge__(self, other: float):
        return self.hp >= other


    def __int__(self):
        return self.hp


    def __str__(self) -> str:
        return f"Health: {self.hp:,}"