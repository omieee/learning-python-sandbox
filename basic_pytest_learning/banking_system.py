class OmBank:
    def __init__(self, balance: float = 0.0) -> None:
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.__balance = self.__balance + amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount > 0 and amount <= self.balance:
            self.__balance = self.__balance - amount
        return self.balance

    def collect_interest(self, interest_rate: float = 1.1) -> float:
        return self.balance * interest_rate
