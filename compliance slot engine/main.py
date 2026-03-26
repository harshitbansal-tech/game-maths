from math_engine import monte_carlo
from volatility import compute
from parsheet import export
from compliance_report import generate
from audit import log

def run(n=1_000_000):
    rtp, wins = monte_carlo(n)
    metrics = compute(wins)
    export(metrics)
    generate(metrics)
    log(metrics)
    return metrics

if __name__ == "__main__":
    print(run(500000))