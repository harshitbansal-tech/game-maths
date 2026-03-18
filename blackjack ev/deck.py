import random

def create_deck(num_decks=6):
    deck = []
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    for _ in range(num_decks):
        for _ in range(4):
            deck.extend(cards)

    random.shuffle(deck)
    return deck


def draw_card(deck):
    return deck.pop()