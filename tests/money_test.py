import unittest
from CardGame.Blackjack.money import Money

class MoneyTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.money = Money(200)
    
    def test_constructor(self) -> None:
        with self.assertRaises(TypeError):
            Money("100")
        with self.assertRaises(TypeError):
            Money(100.0)
        with self.assertRaises(ValueError):
            Money(0)
        with self.assertRaises(ValueError):
            Money(-100)
        self.assertEqual(self.money.value, 200)
        
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()