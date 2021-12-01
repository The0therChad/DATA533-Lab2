# ~/usr/bin/env python3
from CardGame.Cards.card import Card
from CardGame.Cards.deck import Deck
from CardGame.Cards.hand import Hand
from CardGame.Blackjack.person import Player, Dealer
from CardGame.Blackjack.game import Game


def demo():
    print("Demoing the game...")
    # deck = Deck()
    # deck.shuffle()
    blackjack = Game(1)
    # print(blackjack.players[0].hand)

    blackjack.run()


if __name__ == "__main__":
    demo()
