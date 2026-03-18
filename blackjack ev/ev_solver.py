from functools import lru_cache

CARD_VALUES = [2,3,4,5,6,7,8,9,10,10,10,10,11]
PROB = 1 / len(CARD_VALUES)


def adjust(total, soft):
    while total > 21 and soft > 0:
        total -= 10
        soft -= 1
    return total, soft


@lru_cache(None)
def dealer_ev(total, soft):
    total, soft = adjust(total, soft)

    if total > 21:
        return 1

    if total >= 17:
        return -1

    ev = 0
    for c in CARD_VALUES:
        t = total + c
        s = soft + (1 if c == 11 else 0)

        val, sof = adjust(t, s)

        if val > 21:
            ev += PROB * 1
        else:
            ev += PROB * dealer_ev(val, sof)

    return ev


@lru_cache(None)
def stand_ev(player_total, dealer_card):
    ev = 0

    for c in CARD_VALUES:
        dealer_total = dealer_card + c
        dealer_soft = (dealer_card == 11) + (c == 11)

        val, soft = adjust(dealer_total, dealer_soft)

        d_ev = dealer_ev(val, soft)

        if d_ev == 1:
            ev += PROB * 1
        elif d_ev == -1:
            if player_total > val:
                ev += PROB * 1
            elif player_total < val:
                ev += PROB * -1
        else:
            ev += PROB * d_ev

    return ev


@lru_cache(None)
def hit_ev(player_total, soft, dealer_card):
    ev = 0

    for c in CARD_VALUES:
        t = player_total + c
        s = soft + (1 if c == 11 else 0)

        val, sof = adjust(t, s)

        if val > 21:
            ev += PROB * -1
        else:
            ev += PROB * optimal_ev(val, sof, dealer_card)

    return ev


@lru_cache(None)
def optimal_ev(player_total, soft, dealer_card):

    if player_total >= 21:
        return stand_ev(player_total, dealer_card)

    stand = stand_ev(player_total, dealer_card)
    hit = hit_ev(player_total, soft, dealer_card)

    return max(stand, hit)


def generate_ev_table():
    table = {}

    for p in range(4, 22):
        for d in range(2, 12):
            table[(p, d)] = optimal_ev(p, 0, d)

    return table


def generate_strategy_table():
    strat = {}

    for p in range(4, 22):
        for d in range(2, 12):
            s = stand_ev(p, d)
            h = hit_ev(p, 0, d)

            strat[(p, d)] = "HIT" if h > s else "STAND"

    return strat