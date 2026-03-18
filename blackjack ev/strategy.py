def basic_strategy(player, dealer_upcard):
    total = sum(player)

    if total >= 17:
        return "stand"

    if total <= 11:
        return "hit"

    if 12 <= total <= 16:
        if dealer_upcard >= 7:
            return "hit"
        else:
            return "stand"

    return "stand"