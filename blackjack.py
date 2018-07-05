from random import shuffle


def build_deck():
    cards = []
    for i in range(2, 11):
        cards.extend([i] * 4)
    for i in range(3):
        cards.extend([10] * 4)
    cards.extend(['A'] * 4)
    return cards


def shuffle_deck(cards):
    shuffle(cards)
    return cards


def if_ace_player(player_hand):
    while True:
        ace = input('1 or 11?  ')
        if ace == 1 or ace == 11:
            return ace
        else:
            print('invalid input')


def round_start(cards):
    dealer_hand = []
    player_hand = []
    for i in range(2):
        player_hand.append(cards.pop(0))
        dealer_hand.append(
            cards.pop(0))  #second card in dealer's hand has to be face-up
    return player_hand, dealer_hand

def hit_me(player_hand,card):
    player_hand.append(card)

def main():
    cards = shuffle_deck(build_deck())
    while True:
        
    print(round_start(cards)[0])
    print(round_start(cards)[1][1])


main()
