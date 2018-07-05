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


def get_hand_total(hand):  #adds total of deck with ace rules
    non_aces = []
    aces = 0
    for card in hand:
        if card == 'A':
            aces += 1
        else:
            non_aces.append(card)
    non_aces_total = sum(non_aces)
    if aces == 0:
        return non_aces_total
    elif aces == 1:
        if non_aces_total <= 10:
            return non_aces_total + 11
        else:
            return non_aces_total + 1
    elif aces == 2:
        if non_aces_total < 10:
            return non_aces_total + 1 + 11
        else:
            return non_aces_total + 1 + 1
    elif aces == 3:
        if non_aces_total < 9:
            return non_aces_total + 1 + 1 + 11
        else:
            return non_aces_total + 3
    elif aces == 4:
        if non_aces_total < 8:
            return non_aces_total + 1 + 1 + 1 + 11
        else:
            return non_aces_total + 4


def if_blackjack(hand_sum):
    if hand_sum == 21:
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
        elif hit_or_stand == 'show all':
            return hit_or_stand
        else:
            print('Invalid input')


def hit_me(player_hand, card):
    player_hand.append(card)


def change_ace(player_hand):
    player_hand.remove(11)
    player_hand.append(1)


def game_play_player(dealer_hand, player_hand, cards):
    while True:
        player_hand_sum = get_hand_total(player_hand)
        if player_hand_sum > 21:
            print(player_hand)
            print('bust')
            return player_hand_sum
        if if_blackjack(player_hand_sum):
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


def game_play_dealer(dealer_hand, cards):
    while dealer_hand < 21:
        dealer_hand_total = get_hand_total(dealer_hand)
        if 


def big_gameplay(shuffled_cards):
    #if len(shuffled_cards) <= 4:  #if not enough cards to start a game
    #break
    player_hand = round_start_player(shuffled_cards)  #deals 2 cards to player
    dealer_hand = round_start_dealer(shuffled_cards)  #deals 2 cards to dealer
    print(len(shuffled_cards))
    player_hand_sum = game_play_player(dealer_hand, player_hand,
                                       shuffled_cards)
    dealer_sum = game_play_dealer(dealer_hand, shuffled_cards)


def main():
    while True:
        cards = build_deck()
        shuffled_cards = shuffle_deck(cards)
        big_gameplay(shuffled_cards)


if __name__ == '__main__':
    main()
