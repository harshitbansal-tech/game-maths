import numpy as np
from config import BASE_BET, CONTRIBUTION_RATE, START_JACKPOT, HIT_PROB

def simulate_path(n_spins, seed=42):
    rng = np.random.default_rng(seed)
    hits = rng.random(n_spins) < HIT_PROB
    jackpot = START_JACKPOT
    history = np.zeros(n_spins)
    for i in range(n_spins):
        jackpot += BASE_BET * CONTRIBUTION_RATE
        history[i] = jackpot
        if hits[i]:
            break
    return history[:i+1], i+1

def simulate_many(n_paths=10000, n_spins=1_000_000):
    times = []
    finals = []
    for i in range(n_paths):
        h, t = simulate_path(n_spins, seed=i)
        times.append(t)
        finals.append(h[-1])
    return np.array(times), np.array(finals)