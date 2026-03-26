import numpy as np
from config import PAYLINES, PAYTABLE, WILD

def eval_batch(grids):
    n = grids.shape[0]
    total = np.zeros(n)
    for line in PAYLINES:
        symbols = np.array([grids[:,line[i],i] for i in range(5)]).T
        wins = np.zeros(n)
        base = np.full(n, None, dtype=object)
        count = np.zeros(n, dtype=int)
        active = np.ones(n, dtype=bool)
        for i in range(5):
            s = symbols[:,i]
            mask0 = (base == None) & active
            assign = mask0 & (s != WILD)
            base[assign] = s[assign]
            count[mask0] += 1
            match = ((s == base) | (s == WILD)) & active
            count[match & (~mask0)] += 1
            active = active & ((s == base) | (s == WILD) | mask0)
        for sym, table in PAYTABLE.items():
            m = base == sym
            for k,v in table.items():
                wins[(m) & (count>=k)] = v
        total += wins
    return total