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

    def showMoney(self):
        return f"You have ${self.money.value}, and need ${self.money.win} to win."

    def hit_stand(self, dealer):
        if self.hand.getTotalPoints() == 21:
            return False
        status = str(
            input(
                'Please type "hit" to get another card, or "stand" to keep your hand: '
            )
        )
        if status == "hit":
            self.hand.addCard(dealer)
            print("Your hand: ", self.hand)
            if self.hand.getTotalPoints() > 21:
                print("You go bust!")
                for card in self.hand.cards:
                    self.hand.discardHand()
                return False
            elif self.hand.getTotalPoints() == 21:
                print("That's blackjack!")
                return False
            return True
        elif status == "stand":
            print(f"You stand on a hand of {self.hand}")
            return False
        else:
            print("That is not a valid response, please try again.")
            self.hit_stand(dealer)


class Dealer(Player):
    def __init__(self, deck: Deck, hand: Hand = None, money: Money = None) -> None:
        super().__init__(hand=hand, money=money)
        self.deck = deck

    def dealCard(self) -> Card:
        # self.hand = Hand([self.deck.drawCard()])
        # return self.hand
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

    def hit_stand(self, dealer):
        print("Dealer's hand: ", self.hand)
        if self.hand.getTotalPoints() > 21:
            print("The dealer goes bust!")
            self.hand.discardHand()
            return False
        elif self.hand.getTotalPoints() == 21:
            return False
        elif self.hand.getTotalPoints() >= 17:
            print(f"The dealer stands on a hand of {self.hand}")
            return False
        else:
            input("Please press enter to continue.")
            self.hand.addCard(dealer)
            return True
