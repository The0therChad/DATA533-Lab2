#!/usr/bin/env python3
import unittest
from tests.card_test import CardTest
from tests.deck_test import DeckTest
from tests.hand_test import HandTest
from tests.dealer_test import DealerTest
from tests.player_test import PlayerTest
from tests.money_test import MoneyTest

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, buffer=True)
    