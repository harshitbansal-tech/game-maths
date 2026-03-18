import random
from config import REEL_LENGTH

def generate_reel():
    weights = {
        "A": 6, "K": 6, "Q": 6, "J": 6,
        "10": 6, "9": 8, "7": 4
    }

    reel = []
    for sym, count in weights.items():
        reel += [sym] * count

    while len(reel) < REEL_LENGTH:
        reel.append("9")

    random.shuffle(reel)
    return reel[:REEL_LENGTH]


def generate_all_reels():
    return [generate_reel() for _ in range(5)]