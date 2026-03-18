import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(results):
    plt.hist(results, bins=100)
    plt.title("Return Distribution")
    plt.xlabel("Payout")
    plt.ylabel("Frequency")
    plt.show()


def plot_cdf(results):
    sorted_data = np.sort(results)
    y = np.arange(len(results)) / len(results)

    plt.plot(sorted_data, y)
    plt.title("CDF of Returns")
    plt.xlabel("Payout")
    plt.ylabel("CDF")
    plt.show()


def plot_rtp_convergence(results):
    cumulative = np.cumsum(results) / np.arange(1, len(results)+1)

    plt.plot(cumulative)
    plt.title("RTP Convergence")
    plt.xlabel("Spins")
    plt.ylabel("RTP")
    plt.show()