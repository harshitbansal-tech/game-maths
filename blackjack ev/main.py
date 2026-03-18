# main.py

from simulation import play_hand
from deck import create_deck
from metrics import compute_metrics
from config import NUM_SIMULATIONS
from ev_solver import generate_ev_table, generate_strategy_table


def run_simulation():
    results = []
    deck = create_deck()

    for _ in range(NUM_SIMULATIONS):

        if len(deck) < 50:
            deck = create_deck()

        results.append(play_hand(deck))

    return results


def main():

    print("Running Monte Carlo Simulation...\n")
    results = run_simulation()

    metrics = compute_metrics(results)

    print("--- SIMULATION RESULTS ---")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    print("\nGenerating EV Table...\n")
    ev_table = generate_ev_table()

    print("Sample EV values:")
    for k in list(ev_table.keys())[:10]:
        print(k, f"{ev_table[k]:.4f}")

    print("\nGenerating Strategy...\n")
    strategy = generate_strategy_table()

    print("Sample strategy:")
    for k in list(strategy.keys())[:10]:
        print(k, strategy[k])


if __name__ == "__main__":
    main()