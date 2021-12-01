class Money:
    def __init__(self, buyIn: int = 100, win: int = 1000) -> None:
        self.value = buyIn
        self.win = win

    def bet(self):
        amount = None
        amount = input("Please place your bet: ")
        while not amount.isdigit():
            amount = input("That is not an integer. Please place your bet as an integer: ")
        amount = int(amount)
        if amount <= self.value and amount > 0:
            self.value -= amount
        else:
            print("That is not a valid bet, please try again.")
            self.bet()
        return amount

    def payout(self, amount, multiplier):
        self.value += multiplier * amount

    def blackjack(self, amount):
        print(f"That's blackjack!\n You won ${1.5 * amount}!")
        self.value += 2.5 * amount

    def deal_blackjack(self):
        print("The dealer got blackjack!")
