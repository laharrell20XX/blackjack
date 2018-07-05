from random import shuffle


def build_deck():  #creates the deck
    cards = []
    for i in range(2, 11):
        cards.extend([i] * 4)
    for _ in range(3):
        cards.extend([10] * 4)
    cards.extend(['A'] * 4)
    return cards


def shuffle_deck(cards):  #shuffles the deck
    shuffle(cards)
    return cards


def if_ace_player(player_hand):
    for card in player_hand:
        if 'A' in player_hand:
            player_hand.remove('A')
            player_hand.append(11)
    return player_hand


def if_blackjack(hand):
    if sum(hand) == 21:
        return True


def round_start_player(cards):  # starting each round for player
    player_hand = []
    for i in range(2):
        player_hand.append(cards.pop(0))
    return player_hand


def round_start_dealer(cards):  #starting each round for computer
    computer_hand = []
    for i in range(2):
        computer_hand.append(
            cards.pop(0))  # second card in dealer's hand has to be face-up
    return computer_hand


def input_hit_or_stand():  #hit or stand while loop
    while True:
        hit_or_stand = input('hit or stand or show?  ').lower()
        if hit_or_stand == 'hit':
            return hit_or_stand
        elif hit_or_stand == 'stand':
            return hit_or_stand
        elif hit_or_stand == 'show':
            return hit_or_stand
        else:
            print('Invalid input')


def hit_me(player_hand, card):
    player_hand.append(card)


def change_ace(player_hand):
    player_hand.remove(11)
    player_hand.append(1)


def game_play_player(dealer_hand,player_hand, cards):
    while True:
        if_ace_player(player_hand)
        player_hand_sum = sum(player_hand)
        if player_hand_sum > 21:
            if 11 in player_hand:
                change_ace(player_hand)
                continue
            print(player_hand)
            print('bust')
            return player_hand_sum
        if if_blackjack(player_hand):
            return player_hand_sum
        if len(cards) < 1:
            break
        choice = input_hit_or_stand()
        if choice == 'hit':
            hit_me(player_hand, cards.pop(0))
        elif choice == 'show all':
            print('Player has {}'.format(player_hand))
            print('Dealer has [{}, ?]'.format(dealer_hand[1]))
        elif choice == 'stand':
            return player_hand_sum
        print(len(cards))


def game_play_dealer(dealer, cards): #game play for the dealer



def big_gameplay(shuffled_cards):
    while shuffled_cards:
        if len(shuffled_cards) <= 4:  #if not enough cards to start a game
            break
        player_hand = round_start_player(
            shuffled_cards)  #deals 2 cards to player
        dealer_hand = round_start_dealer(
            shuffled_cards)  #deals 2 cards to dealer
        print(len(shuffled_cards))
        player_hand = if_ace_player(player_hand)
        player_hand_sum = game_play_player(dealer_hand,player_hand, shuffled_cards)
        dealer_hand_sum = 


def main():
    while True:
        cards = build_deck()
        shuffled_cards = shuffle_deck(cards)
        big_gameplay(shuffled_cards)

if __name__ == '__main__':
    main()
