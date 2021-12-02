#!/usr/bin/env python3
from CardGame.Blackjack.game import Game


def demo():
    print("Demoing the game... \n")
    blackjack = Game()
    blackjack.run()


if __name__ == "__main__":
    demo()
