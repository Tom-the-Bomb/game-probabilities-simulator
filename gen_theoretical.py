from typing import Callable, Literal
from math import prod

def prod_f(x: int, f: Callable[[int], int]) -> float:
    return prod(f(k) for k in range(1, x))

def P_4(x: int) -> float:
    return (96 * (
        8 * prod_f(x, lambda k: 45 - k)
        + 528 * prod_f(x, lambda k: 41 - k)
        + 9 * prod_f(x, lambda k: 45 - k)
        + 1760 * prod_f(x, lambda k: 37 - k)
    )) / (20_825 * prod_f(x + 1, lambda k: 49 - k))

def P_6(x: int) -> float:
    ...

def theoretical(hand_size: Literal[4, 6]) -> dict[int, float]:
    return {
        x: P_4(x) if hand_size == 4 else P_6(x)
        for x in range(1, 52 - hand_size + 1)
    }