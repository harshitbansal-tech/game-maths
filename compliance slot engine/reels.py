import numpy as np
from config import REELS

def spin_batch(n, seed=42):
    rng = np.random.default_rng(seed)
    reels_len = np.array([len(r) for r in REELS])
    idx = rng.integers(0, reels_len, size=(n,5))
    grids = np.empty((n,3,5), dtype=object)
    for i in range(5):
        reel = REELS[i]
        grids[:,0,i] = reel[(idx[:,i]-1) % len(reel)]
        grids[:,1,i] = reel[idx[:,i]]
        grids[:,2,i] = reel[(idx[:,i]+1) % len(reel)]
    return grids