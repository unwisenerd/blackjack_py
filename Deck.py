#
# cards deck class
#
from random import random
from Cards import Card
from Utilities import get_suits, get_ranks


def get_deck():
    deck = []
    for suit in get_suits():
        for rank in get_ranks():
            deck.append(Card(suit, rank))
    return deck


class Deck:

    def __init__(self):
        self.all_cards = get_deck()

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
