from process import simulate_many
from analytics import expected_time_to_hit, expected_jackpot_at_hit, player_ev, break_even_jackpot, casino_tail_risk
from export import to_excel, to_pdf
from audit import log

def run():
    times, jackpots = simulate_many(5000, 2_000_000)

    metrics = {
        "expected_time_to_hit": expected_time_to_hit(),
        "expected_jackpot_at_hit": expected_jackpot_at_hit(),
        "break_even_jackpot": break_even_jackpot(),
        "avg_simulated_time": times.mean(),
        "avg_simulated_jackpot": jackpots.mean(),
        "tail_risk_10M": casino_tail_risk(jackpots, 10_000_000)
    }

    ev_now = player_ev(jackpots.mean())
    metrics["player_ev_at_avg"] = ev_now

    to_excel({"times": times, "jackpots": jackpots}, "simulation.xlsx")
    to_pdf(metrics, "report.pdf")
    log(metrics)

    return metrics

if __name__ == "__main__":
    print(run())