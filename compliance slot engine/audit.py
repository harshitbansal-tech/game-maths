import json, time, hashlib
from config import REELS, PAYTABLE, PAYLINES

def hash_config():
    return hashlib.sha256(str((REELS, PAYTABLE, PAYLINES)).encode()).hexdigest()

def log(metrics, path="audit_log.json"):
    record = {
        "timestamp": time.time(),
        "config_hash": hash_config(),
        "metrics": metrics
    }
    with open(path,"a") as f:
        f.write(json.dumps(record)+"\n")