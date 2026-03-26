import numpy as np

SYMBOLS = np.array(["A","K","Q","J","10","W","S"])

REELS = [
    np.array(["A","K","Q","J","10","W","A","K","S","Q","J","10"]),
    np.array(["K","Q","J","10","W","A","K","Q","S","J","10","A"]),
    np.array(["Q","J","10","W","A","K","Q","J","S","10","A","K"]),
    np.array(["J","10","W","A","K","Q","J","10","S","A","K","Q"]),
    np.array(["10","W","A","K","Q","J","10","S","A","K","Q","J"])
]

PAYTABLE = {
    "A": {3:5,4:20,5:100},
    "K": {3:4,4:15,5:80},
    "Q": {3:3,4:10,5:60},
    "J": {3:2,4:8,5:50},
    "10": {3:1,4:5,5:40}
}

WILD = "W"

PAYLINES = np.array([
    [1,1,1,1,1],
    [0,0,0,0,0],
    [2,2,2,2,2],
    [0,1,2,1,0],
    [2,1,0,1,2]
])

BET_PER_LINE = 1
TOTAL_BET = BET_PER_LINE * len(PAYLINES)