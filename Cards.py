#
# Class for creating and describing all in-game cards
#
from Utilities import get_rank_values_dict


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = get_rank_values_dict()[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
