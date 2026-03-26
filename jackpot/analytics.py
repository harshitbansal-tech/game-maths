import numpy as np
from config import BASE_BET, CONTRIBUTION_RATE, HIT_PROB, START_JACKPOT

def expected_time_to_hit():
    return 1 / HIT_PROB

def expected_jackpot_at_hit():
    return START_JACKPOT + (BASE_BET * CONTRIBUTION_RATE) / HIT_PROB

def player_ev(jackpot):
    return HIT_PROB * jackpot - BASE_BET

def break_even_jackpot():
    return BASE_BET / HIT_PROB

def casino_tail_risk(jackpots, threshold):
    return np.mean(jackpots >= threshold)