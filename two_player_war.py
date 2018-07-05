from random import shuffle


def if_no_cards(cards, pile):
    if len(cards) == 0:
        shuffle(pile)
        cards.extend(pile.copy())
        pile.clear()


def war_game():
    cards = []
    for i in range(2, 15):
        cards.extend([i] * 4)

    shuffle(cards)

    player_cards = cards[:26]
    computer_cards = cards[26:]
    # for i in cards[:26]:
    #     player_cards.append(i)

    # for i in cards[26:]:
    #     computer_cards.append(i)

    computer_pile = []
    player_pile = []
    war_pile = []
    count = 1
    player_card, computer_card = 0, 0

    while computer_cards and player_cards:
        if player_card and player_card != computer_card:
            print(
                'round {}: draw card (you have {} cards ({}))'.format(
                    count,
                    len(player_cards) + len(player_pile), len(player_cards)),
                end=' ')
            count += 1
            print('(computer has {} cards ({}))'.format(
                len(computer_cards) + len(computer_pile), len(computer_cards)))
        player_card = player_cards.pop(0)
        computer_card = computer_cards.pop(0)
        print('{} for player, {} for computer'.format(player_card,
                                                      computer_card))
        war_pile.extend([player_card, computer_card])
        # while computer_card == player_card:
        if computer_card > player_card:
            computer_pile.extend(war_pile[:])
            war_pile = []
            print("Your {} has lost against the computer's {}. :(".format(
                player_card, computer_card))
        elif computer_card < player_card:
            player_pile.extend(war_pile[:])
            war_pile = []
            print("Your {} has won against the computer's {}!".format(
                player_card, computer_card))
        elif computer_card == player_card:  #if war comes up 1 card before they turn to zero, cards continued to be popped
            print('This. Means. WAR!')
            for i in range(3):
                if_no_cards(player_cards, player_pile)
                if_no_cards(computer_cards, computer_pile)
                if len(player_cards) == 0 or len(computer_cards) == 0:
                    break
                card_1 = (player_cards).pop(0)
                card_2 = (computer_cards).pop(0)
                war_pile.extend([card_1, card_2])

        if len(player_cards) == 0:
            shuffle(player_pile)
            player_cards.extend(player_pile[:])
            player_pile = []
        if len(computer_cards) == 0:
            shuffle(computer_pile)
            computer_cards.extend(computer_pile[:])
            computer_pile = []
        # if_no_cards(player_cards, player_pile)
        # if_no_cards(computer_cards, computer_pile)

        #     input("War never changes...")
        #     player_card = player_cards.pop(0)
        #     computer_card = computer_cards.pop(0)
        #     if computer_card > player_card:
        #         computer_pile.append((player_card, computer_card))
        #         print("Your {} has lost against the computer's {}. :(".format(
        #             player_card, computer_card))
        #     elif computer_card < player_card:
        #         player_pile.append((player_card, computer_card))
        #         print("Your {} has won against the computer's {}!".format(
        #             player_card, computer_card))

    # if len(computer_pile) > len(player_pile):

    if len(computer_cards + computer_pile) > len(player_pile + player_cards):
        print('computer wins')
    else:
        print('player wins')


def main():
    while True:
        input()
        war_game()


if __name__ == '__main__':
    main()