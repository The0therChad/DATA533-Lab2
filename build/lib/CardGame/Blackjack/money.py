class Money:
    win_amount = 1000

    def __init__(self, buy_in: int = 100) -> None:
        if not isinstance(buy_in, int):
            raise TypeError("'buy_in' must be type int")
        if buy_in < 1:
            raise ValueError("'buy_in' must be a positive value")
        self.value = buy_in

    def bet(self) -> int:
        amount = None
        amount = input("Please place your bet: ")
        while not amount.isdigit():
            amount = input("That is not an integer. Please place your bet as an integer: ")
        amount = int(amount)
        if amount <= self.value and amount > 0:
            self.value -= amount
            return amount
        else:
            print("That is not a valid bet, please try again.")
            return self.bet()

    def payout(self, amount: int, multiplier: int or float) -> None:
        if not isinstance(amount, int):
            raise TypeError("'amount' must be type int")
        if type(multiplier) not in (int, float):
            raise TypeError("'multiplier' must be type int or float")
        self.value += int(multiplier * amount)

    def blackjack(self, amount: int) -> None:
        print(f"That's blackjack!\n You won ${1.5 * amount}!")
        self.value += int(2.5 * amount)

    def deal_blackjack(self) -> None:
        print("The dealer got blackjack!")
    
    @classmethod
    def setWin(cls, win_amount: int) -> None:
        if not isinstance(win_amount, int):
            raise TypeError("'win_amount' must be of type int")
        if win_amount < 0:
            raise ValueError("'win_amount' must be a positive integer")
        cls.win_amount = win_amount
