class Balance:  
    def __init__(self, starting_balance: float):
        self.balance = starting_balance
        Balance.instance = self


    def __add__(self, other):
        return self.balance + other

    def __iadd__(self, other):
        self.balance += other
        return self


    def __sub__(self, other):
        return self.balance - other

    def __isub__(self, other: float):
        self.balance -= other
        return self


    def __set__(self, other):
        self.balance = other


    def __lt__(self, other: float):
        return self.balance < other
    
    def __gt__(self, other: float):
        return self.balance > other

    def __le__(self, other: float):
        return self.balance <= other
    
    def __ge__(self, other: float):
        return self.balance >= other


    def __int__(self):
        return self.balance


    def __str__(self) -> str:
        return f"Balance: ${self.balance:,}"