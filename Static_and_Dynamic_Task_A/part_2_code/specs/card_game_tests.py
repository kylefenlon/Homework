import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("hearts", 8)
        self.card2 = Card("spades", 6)
        self.cards = [self.card1, self.card2]
    
    def test_check_for_ace(self):
        result = CardGame.check_for_ace(self, self.card1)
        self.assertFalse(result)

    def test_check_highest_card(self):
        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card1, result)

    def test_number_of_cards(self):
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 14", result)

    
    


