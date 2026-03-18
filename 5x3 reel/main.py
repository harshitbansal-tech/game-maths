from reels import generate_all_reels
from simulation import run_simulation
from metrics import compute_metrics
from analytics import plot_histogram, plot_cdf, plot_rtp_convergence
from config import NUM_SPINS

def main():
    reels = generate_all_reels()

    results = run_simulation(reels, NUM_SPINS)

    metrics = compute_metrics(results)

    print("\n--- SLOT RESULTS ---")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    plot_histogram(results)
    plot_cdf(results)
    plot_rtp_convergence(results)


if __name__ == "__main__":
    main()