import numpy as np

def compute_metrics(results):
    arr = np.array(results)

    rtp = np.mean(arr)
    variance = np.var(arr)
    std = np.std(arr)

    hit_freq = np.mean(arr > 0)

    tail_100 = np.mean(arr >= 100)
    tail_500 = np.mean(arr >= 500)

    return {
        "RTP": rtp,
        "Variance": variance,
        "Std Dev": std,
        "Hit Frequency": hit_freq,
        "P(X>=100)": tail_100,
        "P(X>=500)": tail_500,
        "Max Win": np.max(arr)
    }