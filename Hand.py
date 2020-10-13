#
# player's hand class for holding player'' cards
#
from Utilities import get_rank_values_dict


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0  # sum of all cards in the hand
        self.aces = 0  # for keeping track of aces

    def add_card(self, card):
        # adding card from the Deck.deal()
        self.cards.append(card)
        self.value += get_rank_values_dict()[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    # swapping ace value from 11 to 1 if overall value greater than 21
    def adjust_for_ace(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
