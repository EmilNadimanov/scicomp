#!/usr/bin/python3
from typing import Dict, Callable, Iterable, List
import statistics
from io import TextIOWrapper
from sys import stdin
OPERATIONS: Dict[str, Callable] = {
        'mean': statistics.mean,
        'sum': sum,
        'variance': statistics.variance,
        'median': statistics.median,
        'stddev': statistics.stdev,
        'mad': lambda x: statistics.median(
            map(lambda y: abs(y - statistics.mean(x)),
                x)
            ),
}

def compute(operation: str) -> None:
    sequence = read_from_input()
    print(OPERATIONS[operation](sequence))

def read_from_input() -> List[float]:
    lines = filter(lambda x: x != '',
                   map(str.strip,
                       stdin.readlines()
                   )
            )
    return list(map(float, lines))
    
