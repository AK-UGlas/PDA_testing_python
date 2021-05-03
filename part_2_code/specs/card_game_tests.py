import unittest, pdb
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.deck = [Card(suit, card) for suit in self.suits 
                                       for card in range(1, 14)]

        self.high = Card('Spades', 10)
        self.low = Card('Diamonds', 5)
        self.ace = Card('Spades', 1)
        self.game = CardGame()

    def test_ace(self):
        self.assertTrue(self.game.check_for_ace(self.ace))

    def test_not_ace(self):
        self.assertFalse(self.game.check_for_ace(self.high))

    def test_card1_highest(self):
        self.assertEqual(self.high, self.game.highest_card(self.high, self.low))

    def test_card2_highest(self):
        self.assertEqual(self.high, self.game.highest_card(self.low, self.high))

    def test_correct_card_total(self):
        self.assertEqual("You have a total of 364", self.game.cards_total(self.deck))

    # def test_total_for_one_card(self):
    #     self.assertEqual("You have a total of 10", self.game.cards_total(self.high))
    

    