from ..Cards.card import Card
from ..Cards.deck import Deck
from ..Cards.hand import Hand
from .money import Money


class Player:
    def __init__(self, hand: Hand = None, money: Money = None) -> None:
        self.hand = hand
        self.money = money

    def getHandPoints(self) -> int:
        score = self.hand.getTotalPoints()
        ace_count = len(self.hand.search(rank="A"))
        if ace_count > 1:
            score -= (ace_count - 1) * 10
        return score

    def addToHand(self, hand: Hand) -> None:
        if not isinstance(hand, Hand):
            raise TypeError("'hand' must be type Hand")
        if self.hand is None:
            self.hand = hand
        else:
            self.hand += hand
    
    def addCardToHand(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("'card' must be type Card")
        if self.hand is None:
            self.hand = Hand([card])
        else:
            self.hand.addCard(card)

    def showMoney(self) -> str:
        return f"You have ${self.money.value}, and need ${Money.win_amount} to win."
    
    def discardHand(self) -> None:
        self.hand.discardHand()
    
    def displayHand(self) -> str:
        return f"{str(self.hand)} \t Points: {self.getHandPoints()}"

    def hit_stand(self) -> bool:
        if self.hand.getTotalPoints() == 21:
            print("That's a blackjack!")
            return False
        msg = 'Please type "hit" to get another card, or "stand" to keep your hand: '
        status = input(msg).strip().lower()
        while status not in ("hit", "stand"):
            print("That is not a valid response, please try again.")
            status = input(msg).strip().lower()
        if status == "hit":
            return True
        elif status == "stand":
            print(f"You stand on a hand of {self.displayHand()}")
            return False


class Dealer(Player):
    def __init__(self, deck: Deck, hand: Hand = None, money: Money = None) -> None:
        super().__init__(hand=hand, money=money)
        self.deck = deck

    def dealCard(self) -> Card:
        return self.deck.drawCard()

    def dealHand(self, num_cards: int) -> Hand:
        if not isinstance(num_cards, int):
            raise TypeError("'num_cards' must be an integer")
        if num_cards < 1:
            raise ValueError("'num_cards' must be a positive value")

        if num_cards == 1:
            return Hand([self.dealCard()])
        else:
            return Hand(self.deck.drawCards(min(num_cards, self.deck.size)))

    def hit_stand(self) -> bool:
        print("Dealer's hand: ", self.displayHand())
        if self.getHandPoints() > 21:
            print("The dealer goes bust!\n")
            self.discardHand()
            return False
        elif self.getHandPoints() == 21:
            return False
        elif self.getHandPoints() >= 17:
            print(f"The dealer stands on a hand of {self.displayHand()}\n")
            return False
        else:
            input("Please press enter to continue.")
            return True
