import json, time, hashlib
from config import BASE_BET, CONTRIBUTION_RATE, START_JACKPOT, HIT_PROB

def hash_config():
    return hashlib.sha256(str((BASE_BET, CONTRIBUTION_RATE, START_JACKPOT, HIT_PROB)).encode()).hexdigest()

def log(metrics, path="audit.json"):
    record = {
        "timestamp": time.time(),
        "config_hash": hash_config(),
        "metrics": metrics
    }
    with open(path,"a") as f:
        f.write(json.dumps(record)+"\n")