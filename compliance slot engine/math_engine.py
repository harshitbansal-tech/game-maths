from reels import spin_batch
from evaluator import eval_batch
from config import TOTAL_BET

def monte_carlo(n=1_000_000):
    grids = spin_batch(n)
    wins = eval_batch(grids)
    rtp = wins.mean() / TOTAL_BET
    return rtp, wins