import random
from config import PAYTABLE
from paylines import PAYLINES

def spin(reels):
    positions = [random.randint(0, len(reel)-1) for reel in reels]

    grid = []
    for row in range(3):
        row_symbols = []
        for i in range(5):
            index = (positions[i] + row) % len(reels[i])
            row_symbols.append(reels[i][index])
        grid.append(row_symbols)

    return grid


def evaluate_line(symbols):
    first = symbols[0]
    count = 1

    for s in symbols[1:]:
        if s == first:
            count += 1
        else:
            break

    if count >= 3:
        return PAYTABLE.get(first, {}).get(count, 0)

    return 0


def evaluate_spin(grid):
    total = 0

    for line in PAYLINES:
        symbols = [grid[line[i]-1][i] for i in range(5)]
        total += evaluate_line(symbols)

    return total