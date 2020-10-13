#
# for tracking player's starting chips, bets and ongoing winnings
#

class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    # TODO: add saving of won amount of chips for the next round
    def update_total(self, new_amout):
        self.total = new_amout
