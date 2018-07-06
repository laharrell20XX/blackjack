from random import shuffle


def find_player_bank_account(file1):
    with open(file1, 'r') as file:
        money = int(file.readline())
    return money


def place_ya_bets(money):
    money = find_player_bank_account('bank_account.txt')
    while True:
        player_bet_amount = input(
            'How much do you want to bet? (This is a $20 table; whole dollar amounts only please) '
        )
        if player_bet_amount.isdigit():
            player_bet_amount = int(player_bet_amount)
            if 20 <= player_bet_amount <= money:
                return player_bet_amount
            elif player_bet_amount > money:
                print(
                    "You are trying to bet more than you have.  If this was any other casino, I wouldn't be warning you...\n\n"
                )
        else:
            print('Invalid money amount')


def payout(player_bet_amount, result):
    if result == 'player wins':
        return player_bet_amount
    elif result == 'dealer wins':
        return -player_bet_amount
    elif result == 'push':
        return 0
    elif result == 'Blackjack':
        return player_bet_amount * 1.5


def build_deck():  #creates the deck
    cards = []
    for i in range(2, 11):
        cards.extend([i] * 4)
    for _ in range(3):
        cards.extend([10] * 4)
    cards.extend(['Ace'] * 4)
    return cards


def shuffle_deck(cards):  #shuffles the deck
    shuffle(cards)
    return cards


def get_hand_total(hand):  #adds total of deck with ace rules
    non_aces = []
    aces = 0
    for card in hand:
        if card == 'Ace':
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
        hit_or_stand = input('hit or stand  ').lower()
        if hit_or_stand == 'hit':
            return hit_or_stand
        elif hit_or_stand == 'stand':
            return hit_or_stand
        else:
            print('Invalid input')


def hit_me(player_hand, card):
    player_hand.append(card)


def game_play_player(dealer_hand, player_hand, cards):
    while True:
        player_hand_sum = get_hand_total(player_hand)
        print('\n\nYour cards : {}\n'.format(', '.join(map(str, player_hand))))
        print('\nDealer has {}, ?\n'.format(dealer_hand[1]))
        if player_hand_sum > 21:
            print('\nbust')
            return player_hand_sum
        if if_blackjack(player_hand_sum):
            print('Blackjack!')
            return player_hand_sum
        choice = input_hit_or_stand()
        if choice == 'hit':
            hit_me(player_hand, cards.pop(0))
        elif choice == 'stand':
            return player_hand_sum


def game_play_dealer(dealer_hand, cards, player_hand_sum):
    dealer_hand_total = 0
    while dealer_hand_total <= 21:
        dealer_hand_total = get_hand_total(dealer_hand)
        if dealer_hand_total >= 17 or dealer_hand_total > player_hand_sum:
            break
        dealer_hand.append(cards.pop(0))
    return dealer_hand_total


def winner(player_hand_sum, dealer_hand_sum, player_hand, dealer_hand):
    player_hand_str = ', '.join(map(str, player_hand))
    dealer_hand_str = ', '.join(map(str, dealer_hand))
    if dealer_hand_sum > 21 and player_hand_sum <= 21:
        print('Dealer has busted with a deck of {}!  Player wins! :D'.format(
            dealer_hand_str))
        return 'player wins'
    elif dealer_hand_sum < player_hand_sum <= 21:
        print(
            'Player Wins with a hand of {} against a dealer hand of {}'.format(
                player_hand_str, dealer_hand_str))
        return 'player wins'
    elif player_hand_sum < dealer_hand_sum <= 21:
        print('\nDealer wins with a hand of {} against your hand of {}. :('.
              format(dealer_hand_str, player_hand_str))
        return 'dealer wins'
    elif player_hand_sum == 21:
        return 'Blackjack'
    elif player_hand_sum == dealer_hand_sum:
        print('push')
        return 'push'


def blackjack():  #
    continue_game = True
    while continue_game:
        money = find_player_bank_account('bank_account.txt')
        player_bet_amount = place_ya_bets(money)
        cards = build_deck()
        shuffled_cards = shuffle_deck(cards)
        player_hand = round_start_player(
            shuffled_cards)  #deals 2 cards to player
        player_hand = {'money': 0, 'hand': round_start_player(shuffled_cards)}
        dealer_hand = round_start_dealer(
            shuffled_cards)  #deals 2 cards to dealer
        player_hand_sum = game_play_player(dealer_hand, player_hand,
                                           shuffled_cards)
        dealer_sum = game_play_dealer(dealer_hand, shuffled_cards,
                                      player_hand_sum)
        result = winner(player_hand_sum, dealer_sum, player_hand, dealer_hand)
        game_payout = payout(player_bet_amount, result)
        change_money_amount('bank_account.txt', game_payout, money)
        continue_game = play_again()


def change_money_amount(file1, game_payout, money):
    with open(file1, 'w') as file:
        file.write(str(money + game_payout))


def play_again():
    while True:
        continue_player = input('\nPlay again?\n').lower()
        if 'yes' == continue_player:
            return True
        elif 'no' == continue_player:
            return False
        else:
            print('\nInvalid input\n')


def main():
    blackjack()


if __name__ == '__main__':
    main()
