import numpy as np
from config import TOTAL_BET

def compute(wins):
    mean = wins.mean()
    var = wins.var()
    return {
        "rtp": float(mean / TOTAL_BET),
        "variance": float(var),
        "volatility": float(np.sqrt(var)),
        "hit_frequency": float(np.mean(wins>0)),
        "p_100x": float(np.mean(wins>=100*TOTAL_BET)),
        "p_1000x": float(np.mean(wins>=1000*TOTAL_BET))
    }