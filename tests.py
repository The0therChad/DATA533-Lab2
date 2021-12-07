#!/usr/bin/env python3
import unittest
from tests.card_test import CardTest
from tests.deck_test import DeckTest
from tests.hand_test import HandTest
from tests.dealer_test import DealerTest
from tests.player_test import PlayerTest
from tests.money_test import MoneyTest


def run_tests():
    suite = unittest.TestSuite()
    test_classes = (
        CardTest, DeckTest, HandTest, DealerTest, PlayerTest, MoneyTest
    )
    for test_class in test_classes:
        suite.addTest(unittest.makeSuite(test_class))
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    return runner.run(suite)
    


if __name__ == "__main__":
    result = run_tests()
    print("Success:", result.wasSuccessful())
    