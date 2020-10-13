# blackjack - cards game
#
#
from Chips import Chips
from Deck import Deck
from Hand import Hand


# taking bet from a player
def take_bet(chips):
    while True:

        try:
            chips.bet = int(input('How many chips do you want to bet? '))
        except ValueError:
            print('Sorry, please provide an integer')

        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player Stands, Dealer Turn')
            playing = False
        else:
            print('Sorry, I did not understand that, Please enter h or s only!')
            continue
        break


def show_some(player, dealer):
    print('DEALERS HAND:')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYER HAND:')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print('DEALERS HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)


def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie! PUSH')


if __name__ == '__main__':
    playing = True

    while True:
        # print an opening statement
        print('WELCOME TO BLACKJACK')

        # create and shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle_deck()

        player_hand = Hand()
        player_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

        # Set up player's chips
        player_chips = Chips()

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer's card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this var from hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer's card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out the while loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all dealer's cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print('\nPlayer total chips are at: {}'.format(player_chips.total))

        # Ask to play again
        new_game = input('Would you like to play other hand? y/n: ')

        if new_game[0].lower() == 'y':
            # TODO: add saving of won amount of chips for the next round
            playing = True
            continue
        else:
            print('Thank you for playing!')
            break
