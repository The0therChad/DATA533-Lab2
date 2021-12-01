class Money:
    def __init__(self, buyIn: int = 100, win: int = 1000) -> None:
        self.value = buyIn
        self.win = win

    def bet(self):
        try:
            amount = int(input("Please place your bet: "))
        except ValueError:
            amount = int(
                input("That is not an integer. Please place your bet as an integer: ")
            )
        if amount <= self.value and amount > 0:
            self.value -= amount
        else:
            print("That is not a valid bet, please try again.")
            self.bet()
        return amount

    def blackjack(self, amount):
        print(f"That's blackjack!\n You won ${1.5 * amount}!")
        self.value += 2.5 * amount
