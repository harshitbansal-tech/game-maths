def hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def is_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21


def dealer_play(hand, deck, hit_soft_17=True):
    while True:
        value = hand_value(hand)
        soft = (11 in hand) and value <= 21

        if value < 17:
            hand.append(deck.pop())
        elif value == 17 and soft and hit_soft_17:
            hand.append(deck.pop())
        else:
            break

    return hand