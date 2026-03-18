import numpy as np

def compute_metrics(results):
    arr = np.array(results)

    return {
        "EV (House Edge)": np.mean(arr),
        "Variance": np.var(arr),
        "Std Dev": np.std(arr),
        "Win Rate": np.mean(arr > 0),
        "Loss Rate": np.mean(arr < 0)
    }