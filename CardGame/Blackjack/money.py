class Money:
    def __init__(self, buyIn: int = 100, win: int = 1000) -> None:
        self.value = buyIn
        self.win = win

    def bet(self, amount):
        self.value -= amount
        return amount
