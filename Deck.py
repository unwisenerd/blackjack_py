#
# cards deck class
#
import random
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
        self.deck = get_deck()

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()
